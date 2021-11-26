from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from LocaleSearcher import *
# line 47, 53
food = '떡볶이'

class LSMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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

        self.webEngineView = QWebEngineView()
        self.grid.addWidget(self.webEngineView, 0, 1, 4, 1)  # row, column, row_span, column_span
        #self.webEngineView.load(QUrl("http://localhost/kookminMap/map.html"))
        self.webEngineView.load(QUrl("https://2wodnjs7.github.io/web1/"))
        self.grid.setRowStretch(0, 1)
        self.grid.setRowStretch(1, 1)
        self.grid.setRowStretch(2, 16)
        self.grid.setRowStretch(3, 1)
        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 4)

        self.btnSearch.clicked.connect(self.Search)
        self.lbox.currentItemChanged.connect(self.LboxSelectChanged)
        #self.btnSave.clicked.connect()
        self.show()

    def Search(self):
        self.lbox.clear()
        text = self.query.text()
        x, y, self.locales = SearchLocale(text, food)
        for locale in self.locales:
            self.lbox.addItem(locale.pn)
        self.Move(x, y)

    def LboxSelectChanged(self):
        row = self.lbox.currentRow()
        if row == -1:
            return
        x = self.locales[row].x
        y = self.locales[row].y
        self.Move(x, y)

    def Move(self, x, y):
        page = self.webEngineView.page()
        script = str.format("setMyCenter({0},{1});", y, x)
        page = page.runJavaScript(script)