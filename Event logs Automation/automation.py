import ctypes
import os
import sys
import win32evtlog
import win32evtlogutil
import winerror
from datetime import datetime, timedelta

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def read_recent_event_logs(server='localhost', hours=1):
    log_types = ['Application', 'System', 'Security']
    categorized_events = {log_type: [] for log_type in log_types}
    
    # Calculate the time one hour ago
    one_hour_ago = datetime.now() - timedelta(hours=hours)
    
    for log_type in log_types:
        try:
            hand = win32evtlog.OpenEventLog(server, log_type)
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            while events:
                for event in events:
                    event_time = event.TimeGenerated
                    if event_time >= one_hour_ago:
                        event_data = {
                            'TimeGenerated': event_time.strftime('%Y-%m-%d %H:%M:%S'),
                            'SourceName': event.SourceName,
                            'EventID': winerror.HRESULT_CODE(event.EventID),
                            'EventType': event.EventType,
                            'EventCategory': event.EventCategory,
                            'Message': win32evtlogutil.SafeFormatMessage(event, log_type)
                        }
                        categorized_events[log_type].append(event_data)
                events = win32evtlog.ReadEventLog(hand, flags, 0)
            win32evtlog.CloseEventLog(hand)
            print(f"Successfully read {log_type} logs.")
        except Exception as e:
            print(f"Error reading {log_type} logs: {e}")
    
    return categorized_events

def save_events_to_text(categorized_events, filename='C:\\Users\\kcraq\\Desktop\\Python\\recent_event_logs.txt'):
    try:
        with open(filename, 'w') as file:
            for log_type, events in categorized_events.items():
                file.write(f"\n--- {log_type} Logs ---\n")
                for event in events:
                    file.write(f"Time Generated: {event['TimeGenerated']}\n")
                    file.write(f"Source Name: {event['SourceName']}\n")
                    file.write(f"Event ID: {event['EventID']}\n")
                    file.write(f"Event Type: {event['EventType']}\n")
                    file.write(f"Event Category: {event['EventCategory']}\n")
                    file.write(f"Message: {event['Message']}\n")
                    file.write("-" * 40 + "\n")
        print(f"Event logs saved to {filename}")
    except Exception as e:
        print(f"Error saving the file: {e}")

if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrative privileges to read Security logs.")
        run_as_admin()
        sys.exit()
    
    print("Reading recent event logs...")
    categorized_events = read_recent_event_logs()
    if categorized_events:
        print("Saving recent event logs to text file...")
        save_events_to_text(categorized_events)
    else:
        print("No recent events were read or categorized.")