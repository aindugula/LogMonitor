# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logChecker.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.machinesCombo = QComboBox(self.centralwidget)
        self.machinesCombo.setObjectName(u"machinesCombo")

        self.horizontalLayout.addWidget(self.machinesCombo)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.numLines = QSpinBox(self.centralwidget)
        self.numLines.setObjectName(u"numLines")
        self.numLines.setMinimumSize(QSize(50, 0))
        self.numLines.setMaximum(9999999)

        self.horizontalLayout_2.addWidget(self.numLines)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.search = QLineEdit(self.centralwidget)
        self.search.setObjectName(u"search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy1)
        self.search.setMinimumSize(QSize(50, 0))
        self.search.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.search)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.logContents = QTextEdit(self.centralwidget)
        self.logContents.setObjectName(u"logContents")

        self.verticalLayout.addWidget(self.logContents)


        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.logsList = QListWidget(self.centralwidget)
        self.logsList.setObjectName(u"logsList")

        self.gridLayout.addWidget(self.logsList, 0, 0, 1, 1)

        self.show = QPushButton(self.centralwidget)
        self.show.setObjectName(u"show")

        self.gridLayout.addWidget(self.show, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.quit = QPushButton(self.centralwidget)
        self.quit.setObjectName(u"quit")

        self.gridLayout_2.addWidget(self.quit, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Machines", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.show.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

