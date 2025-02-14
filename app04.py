from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QTextEdit, QPlainTextEdit, QCheckBox, \
    QLabel, QDial


class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.create_menubar()
        self.create_statusbar()
        self.create_central_widget()
        self.show()

    def create_menubar(self):
        pass

    def create_statusbar(self):
        pass
        # self.statusBar().setStyleSheet()

    def create_central_widget(self):
        # center = QLineEdit()
        # center = QTextEdit()
        # center = QPlainTextEdit()
        # center = QCheckBox("Pick me i'm green")
        center = QPushButton('click Me please !')
        # image = QPixmap('Myimg.jpg')
        # center = QLabel('QLabel', pixmap=image)
        # center.setStyleSheet('font-size: 72px; color: green; margin: center')
        center = QDial()
        self.setCentralWidget(center)



app = QApplication([])
window = Mywindow()
app.exec() #excu app 