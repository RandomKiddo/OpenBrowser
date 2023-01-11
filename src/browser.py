from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_dc)
        self.tabs.currentChanged.connect(self.tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        nav = QToolBar('Navigation')
        self.addToolBar(nav)

        back = QAction('<', self)
        back.setStatusTip('Go back to the previous page')
        back.triggered.connect(lambda: self.tabs.currentWidget().back())
        nav.addAction(back)

        fwd = QAction(">", self)
        fwd.setStatusTip('Go forward to the next page')
        fwd.triggered.connect(lambda: self.tabs.currentWidget().forward())
        nav.addAction(fwd)

        reload = QAction('Reload', self)
        reload.setStatusTip('Reload current page')
        reload.triggered.connect(lambda: self.tabs.currentWidget().reload())
        nav.addAction(reload)

        nav.addSeparator()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)
        nav.addWidget(self.url_bar)

        nav.addSeparator()

        add_tab = QAction('+', self)
        add_tab.setStatusTip('Create new tab')
        add_tab.triggered.connect(lambda: self.add_new_tab(url=None, title='New Tab'))
        nav.addAction(add_tab)

        self.add_new_tab(QUrl('https://duckduckgo.com'), 'Homepage')

        self.show()

        self.setWindowTitle('OpenBrowser - © 2023')

    def add_new_tab(self, url=None, title='New Tab'):
        if url is None:
            # creating a google url
            url = QUrl('https://duckduckgo.com')
        browser = QWebEngineView()
        browser.setUrl(url)
        i = self.tabs.addTab(browser, title)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(lambda url, browser=browser: self.update_url_bar(url, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()))

    def tab_open_dc(self, i):
        if i == -1:
            self.add_new_tab()

    def tab_changed(self, i):
        url = self.tabs.currentWidget().url()
        self.update_url_bar(url, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle(title)

    def navigate(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.tabs.currentWidget().setUrl(q)

    def update_url_bar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Geek PyQt5")
    window = MainWindow()
    app.exec_()
