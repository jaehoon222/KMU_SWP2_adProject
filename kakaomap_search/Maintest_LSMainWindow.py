import pickle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from LocaleSearcher import *
from BookMark import BookMark

food = '떡볶이'

class LSMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []
        self.ReadRestaurantDB()

        self.resize(1080, 640)
        self.widget = QWidget()  # QGridLayout개체를 배치할 Widget 개체 생성
        self.setCentralWidget(self.widget)  # LSMainWindow의 CentralWidget 설정
        self.grid = QGridLayout(self.widget)  # QGridLayout 개체 생성

        self.setWindowTitle('내 거주지 주변 음식점 검색')  # 윈도우 타이틀
        self.query = QLineEdit()
        self.query.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.query, 0, 0)
        self.btnSearch = QPushButton()
        self.btnSearch.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnSearch, 1, 0)
        self.btnSearch.setText("내 거주지 입력 및 검색")

        self.lbox = QListWidget()
        self.grid.addWidget(self.lbox, 2, 0)  # row, column, row_span, column_span

        self.btnSave = QPushButton()
        self.btnSave.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnSave, 3, 0)
        self.btnSave.setText("해당 음식점 저장")

        self.btnBookmark = QPushButton()
        self.btnBookmark.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnBookmark, 4, 0)
        self.btnBookmark.setText("즐겨찾기 보기")

        self.webEngineView = QWebEngineView()
        self.grid.addWidget(self.webEngineView, 0, 1, 5, 1)  # row, column, row_span, column_span
        #self.webEngineView.load(QUrl("http://localhost/kookminMap/map.html"))
        self.webEngineView.load(QUrl("https://2wodnjs7.github.io/web1/"))
        self.grid.setRowStretch(0, 1)
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 16)
        self.grid.setRowStretch(3, 1)
        self.grid.setRowStretch(4, 1)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 4)

        self.btnSearch.clicked.connect(self.Search)
        self.lbox.currentItemChanged.connect(self.LboxSelectChanged)
        self.btnSave.clicked.connect(self.RestaurantSave)
        self.btnBookmark.clicked.connect(self.BookmarkMove)


    def ReadRestaurantDB(self):
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

    def Search(self):
        self.lbox.clear()
        text = self.query.text()
        x, y, self.locales = SearchLocale(text, food)
        for locale in self.locales:
            self.lbox.addItem(locale.place_name)
        self.Move(x, y)

    def LboxSelectChanged(self):
        row = self.lbox.currentRow()
        if row == -1:
            return
        x = self.locales[row].x
        y = self.locales[row].y
        self.Move(x, y)

    def RestaurantSave(self):
        fH = open(self.dbfilename, 'wb')
        row = self.lbox.currentRow()
        self.restaurantDB.append([food, self.locales[row].place_name, self.locales[row].address_name, self.locales[row].place_url])
        pickle.dump(self.restaurantDB, fH)
        fH.close()

    def BookmarkMove(self):
        #fH = open(self.dbfilename, 'rb')
        #a = pickle.load(fH)
        #print(a)
        #fH.close()
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Move(self, x, y):
        page = self.webEngineView.page()
        script = str.format("setMyCenter({0},{1});", y, x)
        page = page.runJavaScript(script)


class BookMark(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dbfilename = 'foodBookmark.dat'
        self.restaurantDB = []

        self.resize(1080, 640)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.grid = QGridLayout(self.widget)

        self.lbox = QListWidget()
        self.grid.addWidget(self.lbox, 0, 0, 1, 3)

        self.btnDelete = QPushButton()
        self.btnDelete.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnDelete, 1, 2)
        self.btnDelete.setText("해당 음식점 삭제")

        self.btn = QPushButton()
        self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btn, 1, 0)
        self.btn.setText("지도 이동")

        self.btnPrint = QPushButton()
        self.btnPrint.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.grid.addWidget(self.btnPrint, 1, 1)
        self.btnPrint.setText("즐겨찾기 출력")

        self.grid.setRowStretch(0, 10)
        self.grid.setRowStretch(1, 1)
        self.grid.setColumnStretch(0, 4)
        self.grid.setColumnStretch(1, 1)

        self.setLayout(self.grid)

        self.btnPrint.clicked.connect(self.showBookmarkDB)
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
        try:
            self.restaurantDB = pickle.load(fH)
        except:
            pass
        else:
            pass
        self.lbox.clear()
        for p in self.restaurantDB:
            msg = p[0] + ' \t' + p[1] + '\t\t' + p[2] + ' \t' + p[3] + ' \t'
            self.lbox.addItem(msg)

        fH.close()

    def delBookmarkDB(self):
        fH = open(self.dbfilename, 'wb')
        row = self.lbox.currentRow()
        del self.restaurantDB[row]
        pickle.dump(self.restaurantDB, fH)
        fH.close()

        self.showBookmarkDB()

if __name__ == '__main__':
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