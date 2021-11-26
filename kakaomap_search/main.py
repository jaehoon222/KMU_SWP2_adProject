#main.py
import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from LSMainWindow import LSMainWindow
from BookMark import BookMark

def main():
    #app = QApplication(sys.argv)
    #ex = LSMainWindow()
    #sys.exit(app.exec_())

    app = QApplication(sys.argv)

    widget = QStackedWidget()

    lSMainWindow = LSMainWindow()
    bookMark = BookMark()

    widget.addWidget(lSMainWindow)
    widget.addWidget(bookMark)

    widget.setFixedHeight(640)
    widget.setFixedWidth(1080)
    widget.show()

    app.exec_()
if __name__ == '__main__':
    main()