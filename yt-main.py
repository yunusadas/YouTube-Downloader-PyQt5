from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from pytube import YouTube


class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.link=QLineEdit()
        self.setUI()

    def setUI(self):
        # üst ayarlar
        self.ustayarlar()
        # ANAMENU
        self.anamenu()
        self.show()

    def anamenu(self):
        widget = QWidget()

        h_box = QHBoxLayout()
        # Temel element
        yazi = QLabel("Youtube URL")
        self.link = QLineEdit()
        button = QPushButton("İndir")

        button.clicked.connect(self.indir)

        h_box.addWidget(yazi)
        h_box.addWidget(self.link)
        h_box.addWidget(button)

        widget.setLayout(h_box)
        self.setCentralWidget(widget)

    def indir(self):
        url = self.link.text()
        YouTube(url).streams.get_highest_resolution().download()

    def ustayarlar(self):
        self.setWindowTitle("Youtube Video Manager")
        self.setWindowIcon(QIcon("logo.png"))

        # Boyut AYARLARI

        self.setGeometry(300, 300, 600, 150)
        self.setMaximumSize(1000, 300)
        self.setMinimumSize(600, 150)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
