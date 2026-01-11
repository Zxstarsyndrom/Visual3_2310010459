# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(765, 437)
        self.actionData_Admin = QAction(MainWindow)
        self.actionData_Admin.setObjectName(u"actionData_Admin")
        self.actionData_Usaha = QAction(MainWindow)
        self.actionData_Usaha.setObjectName(u"actionData_Usaha")
        self.actionData_Keluarga = QAction(MainWindow)
        self.actionData_Keluarga.setObjectName(u"actionData_Keluarga")
        self.actionData_Pekerja = QAction(MainWindow)
        self.actionData_Pekerja.setObjectName(u"actionData_Pekerja")
        self.actionKesejahteraan = QAction(MainWindow)
        self.actionKesejahteraan.setObjectName(u"actionKesejahteraan")
        self.actionPendampingan = QAction(MainWindow)
        self.actionPendampingan.setObjectName(u"actionPendampingan")
        self.actionresiko = QAction(MainWindow)
        self.actionresiko.setObjectName(u"actionresiko")
        self.actionBAYA = QAction(MainWindow)
        self.actionBAYA.setObjectName(u"actionBAYA")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 765, 25))
        self.menuMENU = QMenu(self.menubar)
        self.menuMENU.setObjectName(u"menuMENU")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMENU.menuAction())
        self.menuMENU.addAction(self.actionData_Admin)
        self.menuMENU.addAction(self.actionData_Usaha)
        self.menuMENU.addAction(self.actionData_Keluarga)
        self.menuMENU.addAction(self.actionData_Pekerja)
        self.menuMENU.addAction(self.actionKesejahteraan)
        self.menuMENU.addAction(self.actionPendampingan)
        self.menuMENU.addAction(self.actionresiko)
        self.menuMENU.addAction(self.actionBAYA)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionData_Admin.setText(QCoreApplication.translate("MainWindow", u"Data Admin", None))
        self.actionData_Usaha.setText(QCoreApplication.translate("MainWindow", u"Data Usaha", None))
        self.actionData_Keluarga.setText(QCoreApplication.translate("MainWindow", u"Data Keluarga", None))
        self.actionData_Pekerja.setText(QCoreApplication.translate("MainWindow", u"Data Pekerja", None))
        self.actionKesejahteraan.setText(QCoreApplication.translate("MainWindow", u"Kesejahteraan", None))
        self.actionPendampingan.setText(QCoreApplication.translate("MainWindow", u"Pendampingan", None))
        self.actionresiko.setText(QCoreApplication.translate("MainWindow", u"resiko", None))
        self.actionBAYA.setText(QCoreApplication.translate("MainWindow", u"BAYA", None))
        self.menuMENU.setTitle(QCoreApplication.translate("MainWindow", u"MENU", None))
    # retranslateUi

