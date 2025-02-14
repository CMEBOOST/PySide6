import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication([]) #สร้าง initialize
window = QMainWindow()  #สร้าง instace ของ window สร้าง object ของ QMainWindow
window.resize(600,400)
window.show()
app.exec()
