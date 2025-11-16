
# pywinauto-ddt-login-testing
Desktop Application Data-Driven Testing (DDT) using pywinauto with a custom Login GUI.

📌 Desktop Application Data-Driven Testing using pywinauto
This project demonstrates Data-Driven Testing (DDT) on a desktop login application using the open-source Python library pywinauto.
pywinauto (for UI automation)
CSV (for test data)
Tkinter desktop app (as AUT)
Python (for test logic, checkpoints & logging)

🚀 Features

✔ Desktop Login Application (Tkinter based)
A simple GUI with:
Username input
Password input
Login button
Result output

✔ Data-Driven Testing (DDT)
Test data stored in CSV file
Script loops through each row
Compares expected vs actual result

✔ pywinauto Automation Script
The script performs:
Window detection
Typing username & password
Clicking login
Checking result text
Logging pass/fail

✔ Logging
Test results stored in:
logs/test_results.txt

📁 Project Structure
pywin/
│
├── login_app.py                 # Desktop Login GUI
├── dist/login_app.exe           # EXE built with PyInstaller
│
├── data/login_data.csv          # Test Data
├── tests/test_login_ddt.py      # Automation Script
│
├── logs/test_results.txt        # Test Output Log
└── README.md                    # Project Documentation


🧩 Project Architecture
┌─────────────────────────────────────┐
│    Login Desktop Application (AUT)  │
│  (Tkinter GUI built in Python)      │
└─────────────────────────────────────┘
                 ▲
                 │ Automate
                 ▼
┌─────────────────────────────────────┐
│        pywinauto Test Script        │
│  - Launch AUT                       │
│  - Identify UI controls             │
│  - Enter username/password          │
│  - Click Login                      │
│  - Read result label                │
│  - Compare expected vs actual       │
└─────────────────────────────────────┘
                 ▲
                 │ Fetch Data
                 ▼
┌─────────────────────────────────────┐
│          CSV Test Data File         │
│ username,password,expected          │
│ admin,12345,Success                 │
│ user1,wrong,Fail                    │
└─────────────────────────────────────┘
                 ▲
                 │ Store Logs
                 ▼
┌─────────────────────────────────────┐
│          Test Results Log           │
│ logs/test_results.txt               │
└─────────────────────────────────────┘

