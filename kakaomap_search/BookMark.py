import pickle
from PyQt5.QtWidgets import *

food = '떡볶이'

class BookMark(QWidget):

    def __init__(self):
        super().__init__()

        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []

        self.resize(1080, 640)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.grid = QGridLayout(self.widget)

        self.lbox = QListWidget()
        self.grid.addWidget(self.lbox, 0, 0, 1, 2)

        self.btnDelete = QPushButton()
        self.btnDelete.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnDelete, 1, 1)
        self.btnDelete.setText("해당 음식점 삭제")

        self.btn = QPushButton()
        self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 1, 0)
        self.btn.setText("해당 음식점 삭제")

        self.grid.setRowStretch(0, 10)
        self.grid.setRowStretch(1, 1)
        self.grid.setColumnStretch(0, 4)
        self.grid.setColumnStretch(1, 1)

        self.setLayout(self.grid)

        self.btn.clicked.connect(self.go)
        self.btnDelete.clicked.connect(self.delBookmarkDB)

        self.readBookmarkDB()
        self.showBookmarkDB()
        self.show()

    def go(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def readBookmarkDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.restaurantDB = []
            return
        try:
            self.restaurantDB = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    def showBookmarkDB(self):
        fH = open(self.dbfilename, 'rb')
        self.lbox.clear()
        for p in self.restaurantDB:
            msg = p[0] + ' \t' + p[1] + '    \t' + p[2] + ' \t' + p[3] + ' \t'
            self.lbox.addItem(msg)

        fH.close()

    def delBookmarkDB(self):
        fH = open(self.dbfilename, 'wb')
        row = self.lbox.currentRow()
        del self.restaurantDB[row]
        pickle.dump(self.restaurantDB, fH)
        fH.close()

        self.showBookmarkDB()




