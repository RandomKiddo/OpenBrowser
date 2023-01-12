# This program is protected by the MIT License © 2023 RandomKiddo

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import validators
import pyautogui

# todo 'goto tab function'
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)  # Call the superclass constructor

        self.tabs = QTabWidget()  # Create tab widget
        self.tabs.setDocumentMode(True)  # Set to document mode
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_dc)  # Define what to do on double click
        self.tabs.currentChanged.connect(self.tab_changed)  # Define what to do on the tab being changed
        self.tabs.setTabsClosable(True)  # Allow tabs to be closed
        self.tabs.tabCloseRequested.connect(self.close_tab)  # Define what to do when closing a tab
        self.setCentralWidget(self.tabs)  # Set the tabs as the central widget

        self.status = QStatusBar()  # Create a status bar
        self.setStatusBar(self.status)

        nav = QToolBar('Navigation')  # Create a navigation bar
        self.addToolBar(nav)

        more = QAction('More', self)  # Create the more button, its tips, and its trigger action
        more.setStatusTip('Click for more')
        more.triggered.connect(lambda: self.expand_more())
        self.more_open = False
        nav.addAction(more)  # Add action to the nav bar

        nav.addSeparator()

        back = QAction('<', self)  # Create the back button, its tips, and its trigger action
        back.setStatusTip('Go back to the previous page')
        back.triggered.connect(lambda: self.tabs.currentWidget().back())
        nav.addAction(back)  # Add action to the nav bar

        reload = QAction('Reload', self)  # Create the reload button, its tips, and its trigger action
        reload.setStatusTip('Reload current page')
        reload.triggered.connect(lambda: self.tabs.currentWidget().reload())
        nav.addAction(reload)  # Add action to the nav bar

        fwd = QAction(">", self)  # Create the forward button, its tips, and its trigger action
        fwd.setStatusTip('Go forward to the next page')
        fwd.triggered.connect(lambda: self.tabs.currentWidget().forward())
        nav.addAction(fwd)  # Add action to the nav bar

        nav.addSeparator()

        self.url_bar = QLineEdit()  # Create the url bar
        self.url_bar.returnPressed.connect(self.navigate)  # Define how to navigate urls
        nav.addWidget(self.url_bar)  # Add widget to the nav bar

        nav.addSeparator()  # Add a separator

        add_tab = QAction('+', self)  # Create the add tab button, its tips, and its trigger action
        add_tab.setStatusTip('Create new tab')
        add_tab.triggered.connect(lambda: self.add_new_tab(url=None, title='New Tab'))
        nav.addAction(add_tab)  # Add action to the nav bar

        self.add_new_tab(QUrl('https://duckduckgo.com'), 'Homepage')  # Create the 'home' tab

        # Create shortcuts
        self.new_tab_sc = QShortcut(QKeySequence('Ctrl+T'), self)  # New tab shortcut
        self.new_tab_sc.activated.connect(lambda: self.add_new_tab())
        self.reload_sc = QShortcut(QKeySequence('Ctrl+R'), self)  # Reload shortcut
        self.reload_sc.activated.connect(lambda: self.tabs.currentWidget().reload())

        u_width, u_height = pyautogui.size()  # Get screen dimensions
        self.setMaximumWidth(u_width)  # Set max width
        self.setMaximumHeight(u_height)  # Set max height

        self.show()  # Show the window

        self.setWindowTitle('OpenBrowser - © 2023')  # Set the window title

    # Create a new tab with the passed url and title
    def add_new_tab(self, url=None, title='New Tab'):
        if url is None:
            url = QUrl('https://duckduckgo.com')
        browser = QWebEngineView()
        browser.setUrl(url)
        i = self.tabs.addTab(browser, title)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(lambda url, browser=browser: self.update_url_bar(url, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()))

    # Open tab on double-click function
    def tab_open_dc(self, i):
        if i == -1:
            self.add_new_tab()

    # Update a tab when its changed
    def tab_changed(self, i):
        url = self.tabs.currentWidget().url()
        self.update_url_bar(url, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    # Close the given tab index
    def close_tab(self, i):
        if self.tabs.count() < 2:
            self.add_new_tab()
        self.tabs.removeTab(i)

    # Update tab title
    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle(title)

    # Navigate to a new url
    def navigate(self):
        text = self.url_bar.text()
        q = QUrl(text)
        if q.scheme() == "":
            q.setScheme("https")
        if not validators.url('https://' + text):
            q = QUrl('https://duckduckgo.com/?q={}'.format(text))
        self.tabs.currentWidget().setUrl(q)

    # Update the url bar
    def update_url_bar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    # Expand the more accordion
    def expand_more(self):
        if self.more_open:  # Close
            pass
        else:  # Open
            vertical = QVBoxLayout()
            hist = QAction('History', self)  # Create the back button, its tips, and its trigger action
            hist.setStatusTip('See search history')
            hist.triggered.connect(self.go_to_history)
            self.setLayout(vertical)

    def go_to_history(self):
        pass

    # Confirm on close function
    def closeEvent(self, a0):
        msg = 'You are attempting to exit.\nAre you sure?'
        reply = QMessageBox.question(self, 'Message', msg, QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()

def set_palette(app):
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

if __name__ == '__main__':  # Only run if this is the file running
    app = QApplication(sys.argv)  # Create the QApplication
    app.setStyle('Fusion')
    set_palette(app)
    app.setApplicationName("OpenBrowser - © 2023")  # Set app name
    window = MainWindow()  # Instantiate the window
    app.exec_()  # Execute
