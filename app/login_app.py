# app/login_app.py
import sys
from PyQt5 import QtWidgets

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login App")
        self.setFixedSize(360, 250)
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout()

        # Username
        layout.addWidget(QtWidgets.QLabel("Username"))
        self.username = QtWidgets.QLineEdit()
        layout.addWidget(self.username)

        # Password
        layout.addWidget(QtWidgets.QLabel("Password"))
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(self.password)

        # Login button
        self.loginbtn = QtWidgets.QPushButton("Login")
        self.loginbtn.clicked.connect(self.do_login)
        layout.addWidget(self.loginbtn)

        # Visible result
        self.result_label = QtWidgets.QLabel("")
        layout.addWidget(self.result_label)

        # HIDDEN result for pywinauto
        self.hidden_result = QtWidgets.QLabel("")
        self.hidden_result.setObjectName("automation_result")
        self.hidden_result.hide()   # hide it

        layout.addWidget(self.hidden_result)

        self.setLayout(layout)

    def do_login(self):
        u = self.username.text().strip()
        p = self.password.text().strip()

        if u == "admin" and p == "12345":
            result = "Success"
        elif u == "user1" and p == "wrong":
            result = "Fail"
        else:
            result = "Invalid Credentials"

        self.result_label.setText(result)
        self.hidden_result.setText(result)   # <-- AUTOMATION ALWAYS GETS THIS!

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = LoginWindow()
    w.show()
    sys.exit(app.exec_())
