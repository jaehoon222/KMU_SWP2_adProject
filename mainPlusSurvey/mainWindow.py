from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('음식 추천')

        self.resize(1080, 640)

        # Bookmark display window
        self.bmbtn = QPushButton()
        self.bmbtn.setText('Bookmark List')
        self.bmbtn.resize(300,300)


        self.rcmdbtn = QPushButton()
        self.rcmdbtn.setText('Recommend')
        self.rcmdbtn.resize(300,300)


        # Layout
        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.bmbtn)
        btnLayout.addWidget(self.rcmdbtn)
        self.setLayout(btnLayout)

    def rcmdClicked(self):
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())