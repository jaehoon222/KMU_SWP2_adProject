from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QPushButton
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.Qt import QLabel
from PyQt5.Qt import QComboBox

class BookmarkWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('dfddfdf')
        self.resize(1080, 640)

        self.questionLabel6 = QLabel('Test1', self)
        self.answerEdit6 = QComboBox(self)
        self.answerEdit6.addItem('test')

        self.questionLabel7 = QLabel('Test2', self)
        self.answerEdit7 = QComboBox(self)
        self.answerEdit7.addItem('test')
        self.questionLabel8 = QLabel('Test3', self)
        self.answerEdit8 = QComboBox(self)
        self.answerEdit8.addItem('test')
        self.questionLabel9 = QLabel('Test4', self)
        self.answerEdit9 = QComboBox(self)
        self.answerEdit9.addItem('test')
        self.questionLabel10 = QLabel('Test5', self)
        self.answerEdit10 = QComboBox(self)
        self.answerEdit10.addItem('test')

        self.prevButton = QPushButton()
        self.prevButton.setText('이전')
        self.nextButton = QPushButton()
        self.nextButton.setText('다음')



        surveyLayout = QGridLayout()
        surveyLayout.addWidget(self.questionLabel6, 0, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit6, 1, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel7, 2, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit7, 3, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel8, 4, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit8, 5, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel9, 6, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit9, 7, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel10, 8, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit10, 9, 0, 1, 3)
        surveyLayout.addWidget(self.prevButton, 10, 1)
        surveyLayout.addWidget(self.nextButton, 10, 2)


        self.setLayout(surveyLayout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = BookmarkWindow()
    ex.show()
    sys.exit(app.exec_())