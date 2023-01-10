from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

from pandas.io import clipboard

class Browser:
    def __init__(self):
        self.window = QWidget()  # Instantiate the widget and set its title (next line)
        self.window.setWindowTitle("RandomKiddo's Web Browser")

        self.layout = QVBoxLayout()  # Set the vertical layout to a box layout
        self.horizontal = QHBoxLayout()  # Set the horizontal layout to a box layout

        self.url_bar = QTextEdit()  # Instantiate the URL bar
        self.url_bar.setMaximumHeight(30)  # Set max height to 30 for URL bar

        self.search = QPushButton("Search")  # Create the search button
        self.search.setMinimumHeight(30)  # Set min height to 30 for the search button

        self.back = QPushButton("<")  # Create the back button
        self.back.setMinimumHeight(30)  # Set min height to 30 for the back button

        self.refresh = QPushButton('Refresh')  # Create the refresh button
        self.refresh.setMinimumHeight(30)  # Set min height to 30 for the refresh button

        self.fwd = QPushButton(">")  # Create the forward button
        self.fwd.setMinimumHeight(30)  # Set min height to 30 for the forward button

        self.more = QPushButton("...")  # Create the more button
        self.more.setMinimumHeight(30)  # Set min height to 30 for the forward button

        self.history = QPushButton("History")  # Create the history button
        self.history.setMinimumHeight(30)  # Set min height to 30 for the history button
        self.history.setMaximumWidth(100)  # Set max width to 100 for the history button
        self.history_list = []  # Instantiate history list

        self.copy = QPushButton("Copy")  # Create the copy button
        self.copy.setMinimumHeight(30)  # Set min height to 30 for the copy button
        self.copy.setMaximumWidth(100)  # Set max width to 100 for the copy button
        self.copy.setMinimumWidth(100)  # Set min width to 30 for the copy button

        self.horizontal.addWidget(self.more)  # Add the widgets
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.search)
        self.horizontal.addWidget(self.back)
        self.horizontal.addWidget(self.refresh)
        self.horizontal.addWidget(self.fwd)

        self.more_box = QVBoxLayout()  # Create the layout for the 'more' tab
        self.more_box.addWidget(self.history)  # Add the widgets and hide them
        self.history.hide()
        self.more_box.addWidget(self.copy)
        self.copy.hide()

        self.browser = QWebEngineView()  # Instantiate the engine view

        self.search.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))  # Connect the search bar to navigation
        self.back.clicked.connect(self.browser.back)  # Connect back button to its browser function
        self.refresh.clicked.connect(self.browser.reload)  # Connect refresh button to its browser function
        self.fwd.clicked.connect(self.browser.forward)  # Connect forward button to its browser function
        self.more.clicked.connect(self.more_func)  # Connect more button to its browser function
        self.more_tracker = False  # Track if 'more' is expanded
        self.copy.clicked.connect(self.copy_url)  # Connect copy button to its browser function

        self.layout.addLayout(self.horizontal, stretch=0)  # Add the horizontal layout
        self.layout.addLayout(self.more_box, stretch=0)  # Add the 'more' box layout
        self.layout.addWidget(self.browser)  # Add the browser itself

        self.browser.setUrl(QUrl('https://duckduckgo.com/?va=b&t=hc'))  # Set default URL to DuckDuckGo

        self.window.setLayout(self.layout)  # Set the window layout
        self.window.show()  # Show the window

    # Navigate to a new page
    def navigate(self, url):
        if not url.startswith('http'):
            url = 'https://' + url
            self.url_bar.setText(url)
            self.history_list.append(url)
        self.browser.setUrl(QUrl(url))

    # Expand and retract the more tab
    def more_func(self):
        if not self.more_tracker:
            self.history.show()
            self.copy.show()
            self.more_tracker = True
        else:
            self.history.hide()
            self.copy.hide()
            self.more_tracker = False

    # Copy the url to the clipboard
    def copy_url(self):
        url = self.url_bar.toPlainText()
        if 'https' not in url:
            url = 'https://' + url
        clipboard.copy(url)
        self.copy.setText('Copied!')
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.copy.setText('Copy'))
        self.timer.start(1500)

if __name__ == '__main__':
    app = QApplication([])  # Create the application
    window = Browser()  # Create the browser
    app.exec()  # Execute the file

