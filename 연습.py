from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout,QMessageBox
text=0
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('당신이 생각한 숫자 입력', self)
        self.btn.clicked.connect(self.buttonClicked)
        self.le = QLineEdit(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn)
        vbox.addWidget(self.le)
        self.setLayout(vbox)

        self.setWindowTitle('Button')
        self.setGeometry(400, 400, 400, 400)
        self.show()

    def buttonClicked(self):
        QMessageBox.about(self, "당신이 생각한 숫자는...................", self.le.text())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())