from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.Qt import QLabel
from PyQt5.Qt import QComboBox

class RecommendWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('추천할 음식 목록')
        self.resize(1080, 640)

        self.rcmdLabel1 = QLabel('1순위', self)
        self.rcmdLabel1.setAlignment(Qt.AlignCenter)
        font1 = self.rcmdLabel1.font()
        font1.setPointSize(font1.pointSize() + 110)
        self.rcmdLabel1.setFont(font1)
        self.rcmdLabel2 = QLabel('2순위', self)
        self.rcmdLabel2.setAlignment(Qt.AlignCenter)
        font2 = self.rcmdLabel2.font()
        font2.setPointSize(font2.pointSize() + 65)
        self.rcmdLabel2.setFont(font2)
        self.rcmdLabel3 = QLabel('3순위', self)
        self.rcmdLabel3.setAlignment(Qt.AlignCenter)
        font3 = self.rcmdLabel3.font()
        font3.setPointSize(font3.pointSize() + 50)
        self.rcmdLabel3.setFont(font3)


        self.exitButton = QPushButton()
        self.exitButton.setText('끌래요:(')
        self.mapButton = QPushButton()
        self.mapButton.setText('지도 볼래요:)')

        self.exitButton.setMaximumHeight(100)
        self.mapButton.setMaximumHeight(100)

        rcmdLayout = QGridLayout()
        rcmdLayout.addWidget(self.rcmdLabel1, 0, 2, 1, 2)
        rcmdLayout.addWidget(self.rcmdLabel2, 0, 0, 1, 2)
        rcmdLayout.addWidget(self.rcmdLabel3, 0, 4, 1, 2)

        rcmdLayout.addWidget(self.exitButton, 1,2)
        rcmdLayout.addWidget(self.mapButton, 1,3)
        self.space = QLabel('', self)
        rcmdLayout.addWidget(self.space, 2, 0)
        rcmdLayout.setRowStretch(0,5)
        rcmdLayout.setRowStretch(1,5)
        rcmdLayout.setRowStretch(2,1)

        self.setLayout(rcmdLayout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = RecommendWindow()
    ex.show()
    sys.exit(app.exec_())