# tests/test_login_ddt.py
import csv
import os
import time
from datetime import datetime
from pywinauto import Application, Desktop

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
APP_PY = os.path.join(BASE_DIR, "app", "login_app.py")  # Change to login_app.py if needed
DATA_FILE = os.path.join(BASE_DIR, "data", "login_data.csv")
LOG_DIR = os.path.join(BASE_DIR, "logs")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
LOG_FILE = os.path.join(LOG_DIR, "results.log")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def start_app():
    exe_path = os.path.join(BASE_DIR, "dist", "login_app.exe")

    if os.path.exists(exe_path):
        cmd = exe_path
    else:
        cmd = ["python", APP_PY]

    print("STARTING WITH:", cmd)
    app = Application(backend="uia").start(cmd)
    time.sleep(1)
    return app

def find_window():
    d = Desktop(backend="uia")
    for _ in range(20):
        for w in d.windows():
            title = (w.window_text() or "").lower()
            if "login app" in title:
                if w.is_visible():
                    return w
        time.sleep(0.2)
    return None

def perform_test(app, username, password):
    win = find_window()
    if not win:
        return "WINDOW NOT FOUND"

    # get edit fields
    edits = win.descendants(control_type="Edit")
    if len(edits) < 2:
        return "EDIT FIELDS NOT FOUND"

    user_edit = edits[0]
    pass_edit = edits[1]

    try:
        user_edit.set_edit_text(username)
        pass_edit.set_edit_text(password)
    except:
        user_edit.wrapper_object().set_focus()
        user_edit.type_keys("^a{BACKSPACE}" + username, with_spaces=True)
        pass_edit.wrapper_object().set_focus()
        pass_edit.type_keys("^a{BACKSPACE}" + password, with_spaces=True)

    # click the login button
    btns = win.descendants(control_type="Button")
    if not btns:
        return "BUTTON NOT FOUND"

    btns[0].click_input()
    time.sleep(0.6)

    # === ⭐ FINAL SAFE METHOD TO READ RESULT ===
    texts = win.descendants(control_type="Text")

    for t in texts:
        if t.element_info.name == "automation_result":
            result = t.window_text().strip()
            return result if result else "NO TEXT FOUND"

    return "NO TEXT FOUND"


def validate(expected, actual):
    return "PASS" if expected.lower() in actual.lower() else "FAIL"

def log_result(username, expected, actual, status):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {username} | Expected={expected} | Actual={actual} | {status}\n")

def generate_report(results):
    out = os.path.join(REPORT_DIR, "report.html")
    rows = []

    for i, r in enumerate(results, start=1):
        rows.append(
            f"<tr>"
            f"<td>{i}</td>"
            f"<td>{r['user']}</td>"
            f"<td>{r['expected']}</td>"
            f"<td>{r['actual']}</td>"
            f"<td>{r['status']}</td>"
            f"</tr>"
        )

    html = """
    <html>
    <head><meta charset='utf-8'><title>DDT Report</title></head>
    <body>
    <h2>Pywinauto DDT Report</h2>
    <table border='1' cellpadding='6'>
    <tr><th>#</th><th>User</th><th>Expected</th><th>Actual</th><th>Status</th></tr>
    """
    html += "\n".join(rows)
    html += "</table></body></html>"

    with open(out, "w", encoding="utf-8") as f:
        f.write(html)

    return out

def main():
    test_data = read_csv(DATA_FILE)
    results = []

    for row in test_data:
        user = row["Username"]
        pwd = row["Password"]
        expected = row["Expected"]

        app = start_app()
        actual = perform_test(app, user, pwd)
        status = validate(expected, actual)
        log_result(user, expected, actual, status)

        results.append({
            "user": user,
            "expected": expected,
            "actual": actual,
            "status": status
        })

        try:
            app.kill()
        except:
            pass

        time.sleep(0.5)

    report = generate_report(results)
    print("Report generated:", report)

if __name__ == "__main__":
    main()
