from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class Myapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(640, 480)
        self.typed = ''
        self.button = QPushButton('Click Me')
        self.setCentralWidget(self.button)
        self.show()
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print('Button clicked')
    def mouseMoveEvent(self, event):
        print(f'{event.pos()}')
        self.statusBar().showMessage(f"{event.pos()}")

    def mousePressEvent(self, event):
        print(f'{event.pos()}')
        self.statusBar().showMessage(f"{event.pos()}")

    def KeyPressEvent(self, event):
        self.typed += event.text()
        self.statusBar().showMessage(self.typed)



app = QApplication([])
window = Myapp()
app.exec()