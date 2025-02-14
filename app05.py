## Lay out
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton, QLabel


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        anime = QPixmap('anime.jpg')
        self.setWindowIcon(anime)
        self.setWindowTitle('Anime Calculator')
        self.resize(400, 600)
        self.create_central_widget()
        self.create_statusbar()
        self.menubar()
        self.show()

    def create_central_widget(self):
        center = QWidget()
        layout = QGridLayout()
        center.setLayout(layout)
        led = QLabel('DISPLAY AREA')
        led.setStyleSheet('background-color: white;')
        layout.addWidget(led, 1, 1, 1, 4)
        labels = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
        ]
        for row in range(2, 6):  # 2 3 4 5 6
            for col in range(1, 5):  #  1 2 3 4
                widget = QPushButton(labels[row-2][col-1])
                widget.setStyleSheet('font-size: 60px')
                layout.addWidget(widget, row, col)
        eq = QPushButton('=')
        eq.setStyleSheet('font-size: 60px')
        self.setCentralWidget(center)

    def create_statusbar(self):
        statusbar = self.statusBar()
        statusbar.showMessage('Calculator ready !')
        # statusbar.setStyleSheet(f'font-size: 20px ;margin-right: center;')

    def menubar(self):
        menubar = self.menuBar()
        menubar.addMenu('&File')
        menubar.addMenu('&Edit')
        menubar.addMenu('&Help')


app = QApplication([])
calc = Calculator()
app.exec()
