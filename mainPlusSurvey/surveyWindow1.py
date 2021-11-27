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

        self.questionLabel1 = QLabel('Test1', self)
        self.answerEdit1 = QComboBox(self)
        self.answerEdit1.addItem('test')

        self.questionLabel2 = QLabel('Test2', self)
        self.answerEdit2 = QComboBox(self)
        self.answerEdit2.addItem('test')
        self.questionLabel3 = QLabel('Test3', self)
        self.answerEdit3 = QComboBox(self)
        self.answerEdit3.addItem('test')
        self.questionLabel4 = QLabel('Test4', self)
        self.answerEdit4 = QComboBox(self)
        self.answerEdit4.addItem('test')
        self.questionLabel5 = QLabel('Test5', self)
        self.answerEdit5 = QComboBox(self)
        self.answerEdit5.addItem('test')

        self.prevButton = QPushButton()
        self.prevButton.setText('이전')
        self.nextButton = QPushButton()
        self.nextButton.setText('다음')



        surveyLayout = QGridLayout()
        surveyLayout.addWidget(self.questionLabel1, 0, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit1, 1, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel2, 2, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit2, 3, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel3, 4, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit3, 5, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel4, 6, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit4, 7, 0, 1, 3)
        surveyLayout.addWidget(self.questionLabel5, 8, 0, 1, 3)
        surveyLayout.addWidget(self.answerEdit5, 9, 0, 1, 3)
        surveyLayout.addWidget(self.prevButton, 10, 1)
        surveyLayout.addWidget(self.nextButton, 10, 2)


        self.setLayout(surveyLayout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = BookmarkWindow()
    ex.show()
    sys.exit(app.exec_())