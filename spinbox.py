<<<<<<< HEAD
import sys
from PySide6.QtWidgets import QWidget,QApplication,QVBoxLayout,QMainWindow,QPushButton,\
QSpinBox,QLabel,QLineEdit
from PySide6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("qspinbox example")
        self.resize(300,400)
        central_widget = QWidget()
        layout = QVBoxLayout()
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(1,12)
        self.spinbox.setValue(1)
        self.spinbox.setSuffix("month")
        self.welcome_label = QLabel("please select month",self)
        self.button = QPushButton("click me",self)
        self.result_label = QLabel(self)
        self.button.clicked.connect(self.on_clicked)

        layout.addWidget(self.welcome_label,alignment=Qt.AlignCenter)
        layout.addWidget(self.spinbox,alignment=Qt.AlignCenter)
        layout.addWidget(self.button,alignment=Qt.AlignCenter)
        layout.addWidget(self.result_label,alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_clicked (self):
        value = self.spinbox.value()
        current_month = 11
        if current_month > value:
            self.result_label.setText(f"your selection : {value} , you selected a past month")
        elif current_month == value :
            self.result_label.setText(f"your selection : {value} , you selected current month")
        else:
            self.result_label.setText(f"your selection : {value} , you selected a future month")

app =  QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()


=======
import sys
from PySide6.QtWidgets import QWidget,QApplication,QVBoxLayout,QMainWindow,QPushButton,\
QSpinBox,QLabel,QLineEdit
from PySide6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("qspinbox example")
        self.resize(300,400)
        central_widget = QWidget()
        layout = QVBoxLayout()
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(1,12)
        self.spinbox.setValue(1)
        self.spinbox.setSuffix("month")
        self.welcome_label = QLabel("please select month",self)
        self.button = QPushButton("click me",self)
        self.result_label = QLabel(self)
        self.button.clicked.connect(self.on_clicked)

        layout.addWidget(self.welcome_label,alignment=Qt.AlignCenter)
        layout.addWidget(self.spinbox,alignment=Qt.AlignCenter)
        layout.addWidget(self.button,alignment=Qt.AlignCenter)
        layout.addWidget(self.result_label,alignment=Qt.AlignCenter)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_clicked (self):
        value = self.spinbox.value()
        current_month = 11
        if current_month > value:
            self.result_label.setText(f"your selection : {value} , you selected a past month")
        elif current_month == value :
            self.result_label.setText(f"your selection : {value} , you selected current month")
        else:
            self.result_label.setText(f"your selection : {value} , you selected a future month")

app =  QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()


>>>>>>> 3270cc8c0b9c55d79a9190245425dad0b5445038
