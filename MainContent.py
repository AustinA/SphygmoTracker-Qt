from PySide2.QtWidgets import QWidget
from ui import Ui_mainContent


class MainContent(QWidget):
    def __init__(self):
        super(MainContent, self).__init__()
        self.ui = Ui_mainContent()
        self.ui.setupUi(self)
