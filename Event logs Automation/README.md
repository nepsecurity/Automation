# Windows Event Log Reader

A Python script to read recent Windows Event Logs (from the last hour) and save them to a text file.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This script reads Windows Event Logs from the `Application`, `System`, and `Security` logs, filters them to include only those generated in the last hour, and saves them to a text file. It requires administrative privileges to read the `Security` logs.

## Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
- **pywin32**: This library provides access to many of the Windows API functions. You can install it using `pip`.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/windows-event-log-reader.git
   cd windows-event-log-reader
2. Install Required Libraries:
   pip install pywin32

3. Usage
Open Command Prompt or PowerShell as Administrator:
Press Win + X and select "Command Prompt (Admin)" or "Windows PowerShell (Admin)".
Alternatively, right-click on the Command Prompt or PowerShell icon in the Start menu and select "Run as administrator".
Navigate to the Script Directory:
cd path\to\windows-event-log-reader
Run the Script:
python automation.py

4. Verify the Output:
The script will save the recent event logs to a text file named recent_event_logs.txt on your desktop.
Open the file to verify the contents.


### Additional Files

- **`CONTRIBUTING.md`**: A file explaining how to contribute to the project.
- **`LICENSE`**: A file containing the MIT License text.

This README provides a concise overview of the project, setup instructions, and usage, making it easy for users to get started with the script.
