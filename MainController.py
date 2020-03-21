from PySide2.QtCore import QObject, QModelIndex, QDir, QAbstractItemModel
from PySide2.QtWidgets import QVBoxLayout, QHeaderView, QAbstractItemView, QMessageBox, QFileDialog, QTableWidgetItem
from MainWindow import MainWindow
from MainContent import MainContent
from helpers.Utilities import *
import csv


class MainController(QObject):
    def __init__(self):
        QObject.__init__(self)

        # Initialize visual elements
        self.mainWindow = MainWindow()
        self.mainContent = MainContent()

        # Add Main Content ot Main Window
        layout = QVBoxLayout()
        layout.insertWidget(0, self.mainContent)
        self.mainWindow.ui.centralwidget.setLayout(layout)

        # Initialize the menu actions
        self.__initializeMenuActions()

        # Initialize the button and their signals
        self.__initializeButtons()

        # Initialize the table widget
        self.__initializeTableWidget()

    def showWindow(self):
        self.mainWindow.show()

    ######### Private Functions #########
    #####################################

    def __initializeMenuActions(self):
        self.mainWindow.ui.actionOpen.triggered.connect(self.__handleActionOpened)
        self.mainWindow.ui.actionSave_As.triggered.connect(self.__handleActionSaveAs)

    def __initializeButtons(self):
        # Connect the signals to slots
        self.mainContent.ui.addBtn.pressed.connect(self.__handleAddBtnPressed)
        self.mainContent.ui.deleteBtn.pressed.connect(self.__handleDeleteBtnPressed)
        self.mainContent.ui.clearBtn.pressed.connect(self.__handleClearBtnPressed)

    def __initializeTableWidget(self):
        self.tableWidget = self.mainContent.ui.tableWidget

        # Create the column count and headers
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Date", "Systolic (mmHg)", "Diastolic (mmHg)", "Heart rate (BBM)"])

        # Stretch the columns to the size of the parent
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Set the triggers and selection behaviors
        self.tableWidget.setEditTriggers(QAbstractItemView.CurrentChanged)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)


    # Ideally, this should really be based off a QAbstractItemModel, but we're cheating because this is just an
    # an example program
    def __saveEntries(self):
        fileName = QFileDialog.getSaveFileName(self.mainWindow, "Save Entries", QDir.homePath() + "/vitals_history.csv",
                                               "CSV Files(*.csv *.txt)")
        if fileName[0]:
            output_string = ""
            for i in range(self.tableWidget.rowCount()):
                for j in range(self.tableWidget.columnCount()):
                    widgetItem = self.tableWidget.item(i, j)  # type: QTableWidgetItem
                    theText = widgetItem.text()
                    if j == self.tableWidget.columnCount() - 1:
                        output_string = output_string + theText
                    else:
                        output_string = output_string + theText + ","
                output_string = output_string + "\n"

            file = open(fileName[0], "w+")
            file.write(output_string)
            file.close()

    def __openEntries(self):
        didRemoveRows = False
        if self.tableWidget.rowCount() > 0:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Clear current entries?")
            messageBox.setText("Opening a record will delete the current entries. Continue?")
            messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            result = messageBox.exec_()
            if result == QMessageBox.Ok:
                didRemoveRows = True
                model = self.tableWidget.model()  # type: QAbstractItemModel
                for i in range(self.tableWidget.rowCount()):
                    model.removeRow(i)

        if self.tableWidget.rowCount() == 0 or didRemoveRows:
            fileName = QFileDialog.getOpenFileName(self.mainWindow, "Open Entry", QDir.homePath(),
                                                   "CSV Files(*.csv *.txt)")
            if fileName[0]:
                with open(fileName[0]) as csvfile:
                    reader = csv.reader(csvfile, delimiter=",")
                    for row in reader:
                        self.tableWidget.insertRow(self.tableWidget.rowCount())
                        model = self.tableWidget.model()
                        for j in range(self.tableWidget.columnCount()):
                            model.setData(model.index(self.tableWidget.rowCount() - 1, j), row[j])

    ######### SLOTS #########
    #########################

    def __handleClearBtnPressed(self):
        # Set the current index to a non-existant cell to de-select everything
        self.tableWidget.setCurrentCell(-1, -1)

    def __handleAddBtnPressed(self):
        # Insert a new row
        self.tableWidget.insertRow(self.tableWidget.rowCount())

        # Auto-complete the date and time for the entry
        model = self.tableWidget.model()
        model.setData(model.index(self.tableWidget.rowCount() - 1, 0), TimeHelper.getCurrentTimeStamp())

        # Set the new current index to the next editable cell after auto-completing the date
        index = self.tableWidget.model().index(self.tableWidget.rowCount() - 1, 1)
        self.tableWidget.setCurrentIndex(index)

    def __handleDeleteBtnPressed(self):
        index = self.tableWidget.currentIndex()  # type: QModelIndex

        # If something has been selected, prompt the user to verify if deletion is desired
        if index.row() != -1 and index.column() != -1:
            # Present warning box to delete a row
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Delete Entry?")
            messageBox.setText("Are you sure you want to delete the entry?")
            messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            if messageBox.exec_() == QMessageBox.Ok:
                self.tableWidget.removeRow(self.tableWidget.currentRow())

    def __handleActionOpened(self):
        self.__openEntries()

    def __handleActionSaveAs(self):
        self.__saveEntries()
