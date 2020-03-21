#!/usr/bin/env python

from PySide2.QtWidgets import QApplication
import sys
from MainController import MainController

def main():
    # Create the main application loop
    app = QApplication(sys.argv)

    mainController = MainController()
    mainController.showWindow()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()