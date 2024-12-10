<<<<<<< HEAD
import sys
from PySide6.QtWidgets import QWidget,QApplication,QVBoxLayout,QMainWindow,QPushButton,\
QProgressBar,QLabel,QLineEdit
from PySide6.QtCore import Qt,QTimer


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("qprogressbar example")
        self.resize(300,400)
        central_widget = QWidget()
        layout = QVBoxLayout()



        self.progressbar = QProgressBar(self)
        self.progressbar.setRange(0,100)
        self.progressbar.setValue(0)
        self.progressbar.setTextVisible(True)
        self.button = QPushButton("start task",self)
        self.button.clicked.connect(self.start_task)


        layout.addWidget(self.progressbar)
        layout.addWidget(self.button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


        self.time = QTimer(self)
        self.time.timeout.connect(self.update_percentage)
        self.progress_value = 0

    def start_task(self):
        self.button.setEnabled(False)
        self.time.start(500)

    def update_percentage(self):
        self.progress_value +=20
        self.progressbar.setValue(self.progress_value)
        if self.progress_value>=100:
            self.time.stop()
            self.button.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
=======
import sys
from PySide6.QtWidgets import QWidget,QApplication,QVBoxLayout,QMainWindow,QPushButton,\
QProgressBar,QLabel,QLineEdit
from PySide6.QtCore import Qt,QTimer


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("qprogressbar example")
        self.resize(300,400)
        central_widget = QWidget()
        layout = QVBoxLayout()



        self.progressbar = QProgressBar(self)
        self.progressbar.setRange(0,100)
        self.progressbar.setValue(0)
        self.progressbar.setTextVisible(True)
        self.button = QPushButton("start task",self)
        self.button.clicked.connect(self.start_task)


        layout.addWidget(self.progressbar)
        layout.addWidget(self.button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


        self.time = QTimer(self)
        self.time.timeout.connect(self.update_percentage)
        self.progress_value = 0

    def start_task(self):
        self.button.setEnabled(False)
        self.time.start(500)

    def update_percentage(self):
        self.progress_value +=20
        self.progressbar.setValue(self.progress_value)
        if self.progress_value>=100:
            self.time.stop()
            self.button.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
>>>>>>> 3270cc8c0b9c55d79a9190245425dad0b5445038
    main()