from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

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

        self.fwd = QPushButton(">")  # Create the forward button
        self.fwd.setMinimumHeight(30)  # Set min height to 30 for the forward button

        self.horizontal.addWidget(self.url_bar)  # Add the widgets
        self.horizontal.addWidget(self.search)
        self.horizontal.addWidget(self.back)
        self.horizontal.addWidget(self.fwd)

        self.browser = QWebEngineView()  # Instantiate the engine view

        self.search.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back.clicked.connect(self.browser.back)
        self.fwd.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal, stretch=0)  # Add the horizontal layout
        self.layout.addWidget(self.browser)  # Add the browser itself

        self.browser.setUrl(QUrl('https://duckduckgo.com/?va=b&t=hc'))  # Set default URL to DuckDuckGo

        self.window.setLayout(self.layout)  # Set the window layout
        self.window.show()  # Show the window

    def navigate(self, url):
        if not url.startswith('http'):
            url = 'https://' + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication([])  # Create the application
    window = Browser()  # Create the browser
    app.exec()  # Execute the file

