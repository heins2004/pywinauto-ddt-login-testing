import csv
from pywinauto.application import Application
import time
import os

# Make sure logs folder exists
if not os.path.exists("../logs"):
    os.makedirs("../logs")

# Start login application
app = Application().start(r"C:\Users\hp\Desktop\pywin\dist\login_app.exe")
time.sleep(1)

dlg = app.window(title="Login")

log_file = open("../logs/test_results.txt", "w")

with open("../data/login_data.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        username = row["username"]
        password = row["password"]
        expected = row["expected"]

        dlg.UsernameEdit.set_edit_text(username)
        dlg.PasswordEdit.set_edit_text(password)
        dlg.LoginButton.click()

        time.sleep(0.5)
        actual = dlg.Static3.window_text()

        if actual == expected:
            result = f"[PASS] {username} -> Expected: {expected}, Got: {actual}"
        else:
            result = f"[FAIL] {username} -> Expected: {expected}, Got: {actual}"

        print(result)
        log_file.write(result + "\n")

log_file.close()
print("Test completed! Check logs folder.")
