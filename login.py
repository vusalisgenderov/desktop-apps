
import sys
from PySide6.QtWidgets import (
    QCheckBox, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QStackedWidget, QPushButton, QMessageBox, QMainWindow
)
from PySide6.QtCore import Qt

# İstifadəçilər üçün verilənlər bazası
db = [
    {"username": "kenan", "password": "kenan123", "isadmin": True},
    {"username": "orxan", "password": "orxan123", "isadmin": False}
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.resize(400, 600)

        self.stacked_widget = QStackedWidget()
        self.login_widget = QWidget()
        self.admin_widget = QWidget()
        self.user_widget = QWidget()

        self.username = QLineEdit()
        self.username.setPlaceholderText("Input a username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Input a password")
        self.password.setEchoMode(QLineEdit.Password)

        self.checkbox = QCheckBox("Login as admin")
        self.button = QPushButton("Login")
        self.button.setEnabled(True)
        self.button.clicked.connect(self.login_func)

        login_layout = QVBoxLayout()
        admin_layout = QVBoxLayout()
        user_layout = QVBoxLayout()

        login_layout.addWidget(self.username)
        login_layout.addWidget(self.password)
        login_layout.addWidget(self.checkbox)
        login_layout.addWidget(self.button)

        self.admin_label = QLabel("This is the admin page")
        self.admin_label.setAlignment(Qt.AlignCenter)
        admin_layout.addWidget(self.admin_label)

        self.user_label = QLabel("This is the user page")
        self.user_label.setAlignment(Qt.AlignCenter)
        user_layout.addWidget(self.user_label)

        self.admin_widget.setLayout(admin_layout)
        self.user_widget.setLayout(user_layout)

        self.login_widget.setLayout(login_layout)
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.admin_widget)
        self.stacked_widget.addWidget(self.user_widget)

        self.setCentralWidget(self.stacked_widget)

    def login_func(self):
        username = self.username.text().strip()
        password = self.password.text().strip()
        value_of_checkbox = self.checkbox.isChecked()

        for user in db:
            if username == user['username'] and password == user['password'] and value_of_checkbox == user['isadmin']:
                if value_of_checkbox:  
                    self.stacked_widget.setCurrentWidget(self.admin_widget)
                else: 
                    self.stacked_widget.setCurrentWidget(self.user_widget)
                return  
        
        QMessageBox.warning(self, "Login Failed", "Invalid username, password, or role!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

import sys
from PySide6.QtWidgets import (
    QCheckBox, QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QStackedWidget, QPushButton, QMessageBox, QMainWindow
)
from PySide6.QtCore import Qt

# İstifadəçilər üçün verilənlər bazası
db = [
    {"username": "kenan", "password": "kenan123", "isadmin": True},
    {"username": "orxan", "password": "orxan123", "isadmin": False}
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.resize(400, 600)

        self.stacked_widget = QStackedWidget()
        self.login_widget = QWidget()
        self.admin_widget = QWidget()
        self.user_widget = QWidget()

        self.username = QLineEdit()
        self.username.setPlaceholderText("Input a username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Input a password")
        self.password.setEchoMode(QLineEdit.Password)

        self.checkbox = QCheckBox("Login as admin")
        self.button = QPushButton("Login")
        self.button.setEnabled(True)
        self.button.clicked.connect(self.login_func)

        login_layout = QVBoxLayout()
        admin_layout = QVBoxLayout()
        user_layout = QVBoxLayout()

        login_layout.addWidget(self.username)
        login_layout.addWidget(self.password)
        login_layout.addWidget(self.checkbox)
        login_layout.addWidget(self.button)

        self.admin_label = QLabel("This is the admin page")
        self.admin_label.setAlignment(Qt.AlignCenter)
        admin_layout.addWidget(self.admin_label)

        self.user_label = QLabel("This is the user page")
        self.user_label.setAlignment(Qt.AlignCenter)
        user_layout.addWidget(self.user_label)

        self.admin_widget.setLayout(admin_layout)
        self.user_widget.setLayout(user_layout)

        self.login_widget.setLayout(login_layout)
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.admin_widget)
        self.stacked_widget.addWidget(self.user_widget)

        self.setCentralWidget(self.stacked_widget)

    def login_func(self):
        username = self.username.text().strip()
        password = self.password.text().strip()
        value_of_checkbox = self.checkbox.isChecked()

        for user in db:
            if username == user['username'] and password == user['password'] and value_of_checkbox == user['isadmin']:
                if value_of_checkbox:  
                    self.stacked_widget.setCurrentWidget(self.admin_widget)
                else: 
                    self.stacked_widget.setCurrentWidget(self.user_widget)
                return  
        
        QMessageBox.warning(self, "Login Failed", "Invalid username, password, or role!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

