# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainContent.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_mainContent(object):
    def setupUi(self, mainContent):
        if mainContent.objectName():
            mainContent.setObjectName(u"mainContent")
        mainContent.resize(588, 447)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(mainContent.sizePolicy().hasHeightForWidth())
        mainContent.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(mainContent)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(mainContent)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.addBtn = QPushButton(mainContent)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setMinimumSize(QSize(20, 0))
        self.addBtn.setMaximumSize(QSize(120, 30))

        self.horizontalLayout.addWidget(self.addBtn)

        self.deleteBtn = QPushButton(mainContent)
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.deleteBtn.setMaximumSize(QSize(140, 30))

        self.horizontalLayout.addWidget(self.deleteBtn)

        self.clearBtn = QPushButton(mainContent)
        self.clearBtn.setObjectName(u"clearSelection")
        self.clearBtn.setMaximumSize(QSize(140, 30))

        self.horizontalLayout.addWidget(self.clearBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(mainContent)

        QMetaObject.connectSlotsByName(mainContent)
    # setupUi

    def retranslateUi(self, mainContent):
        mainContent.setWindowTitle(QCoreApplication.translate("mainContent", u"Form", None))
        self.addBtn.setText(QCoreApplication.translate("mainContent", u"Add Entry", None))
        self.deleteBtn.setText(QCoreApplication.translate("mainContent", u"Delete Selected", None))
        self.clearBtn.setText(QCoreApplication.translate("mainContent", u"Clear Selection", None))
    # retranslateUi

