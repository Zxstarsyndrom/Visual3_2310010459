# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Baya.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(892, 586)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(240, 60, 311, 181))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.kodeLabel = QLabel(self.formLayoutWidget)
        self.kodeLabel.setObjectName(u"kodeLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.kodeLabel)

        self.kodeLineEdit = QLineEdit(self.formLayoutWidget)
        self.kodeLineEdit.setObjectName(u"kodeLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.kodeLineEdit)

        self.nAMABARANGLabel = QLabel(self.formLayoutWidget)
        self.nAMABARANGLabel.setObjectName(u"nAMABARANGLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nAMABARANGLabel)

        self.nAMABARANGLineEdit = QLineEdit(self.formLayoutWidget)
        self.nAMABARANGLineEdit.setObjectName(u"nAMABARANGLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nAMABARANGLineEdit)

        self.hARGALabel = QLabel(self.formLayoutWidget)
        self.hARGALabel.setObjectName(u"hARGALabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.hARGALabel)

        self.hARGALineEdit = QLineEdit(self.formLayoutWidget)
        self.hARGALineEdit.setObjectName(u"hARGALineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.hARGALineEdit)

        self.jUMLAHLabel = QLabel(self.formLayoutWidget)
        self.jUMLAHLabel.setObjectName(u"jUMLAHLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.jUMLAHLabel)

        self.jUMLAHLineEdit = QLineEdit(self.formLayoutWidget)
        self.jUMLAHLineEdit.setObjectName(u"jUMLAHLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.jUMLAHLineEdit)

        self.tOTALLabel = QLabel(self.formLayoutWidget)
        self.tOTALLabel.setObjectName(u"tOTALLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tOTALLabel)

        self.tOTALLineEdit = QLineEdit(self.formLayoutWidget)
        self.tOTALLineEdit.setObjectName(u"tOTALLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tOTALLineEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(290, 250, 90, 29))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(420, 250, 90, 29))
        self.tablebaya = QTableWidget(Form)
        if (self.tablebaya.columnCount() < 5):
            self.tablebaya.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablebaya.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablebaya.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablebaya.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablebaya.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablebaya.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tablebaya.setObjectName(u"tablebaya")
        self.tablebaya.setGeometry(QRect(70, 340, 631, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.kodeLabel.setText(QCoreApplication.translate("Form", u"kode", None))
        self.nAMABARANGLabel.setText(QCoreApplication.translate("Form", u"NAMA BARANG", None))
        self.hARGALabel.setText(QCoreApplication.translate("Form", u"HARGA", None))
        self.jUMLAHLabel.setText(QCoreApplication.translate("Form", u"JUMLAH", None))
        self.tOTALLabel.setText(QCoreApplication.translate("Form", u" TOTAL +DISKON 7%", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tablebaya.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"KODE", None));
        ___qtablewidgetitem1 = self.tablebaya.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"NAMA_BARANG", None));
        ___qtablewidgetitem2 = self.tablebaya.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"HARGA", None));
        ___qtablewidgetitem3 = self.tablebaya.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"JUMLAH", None));
        ___qtablewidgetitem4 = self.tablebaya.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"TOTAL", None));
    # retranslateUi

