#main.py
import sys
from PyQt5.QtWidgets import QApplication
from BookMark import BookMark
def main():
    app = QApplication(sys.argv)
    ex = BookMark()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
