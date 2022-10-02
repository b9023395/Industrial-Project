from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        screen = QApplication.primaryScreen()
        size = screen.size()
        self.setGeometry(int(size.width()/2)-300, int(size.height()/2)-300, 600, 600)
        self.setWindowTitle("GUI Window")
        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())