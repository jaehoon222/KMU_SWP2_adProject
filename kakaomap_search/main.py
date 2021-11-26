#main.py
import sys
from PyQt5.QtWidgets import QApplication
from LSMainWindow import LSMainWindow
def main():
    app = QApplication(sys.argv)
    ex = LSMainWindow()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()