# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataUsaha.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(551, 598)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.iDUSAHALabel = QLabel(Form)
        self.iDUSAHALabel.setObjectName(u"iDUSAHALabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDUSAHALabel)

        self.iDUSAHALineEdit = QLineEdit(Form)
        self.iDUSAHALineEdit.setObjectName(u"iDUSAHALineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.iDUSAHALineEdit)

        self.nAMAUSAHALabel = QLabel(Form)
        self.nAMAUSAHALabel.setObjectName(u"nAMAUSAHALabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nAMAUSAHALabel)

        self.nAMAUSAHALineEdit = QLineEdit(Form)
        self.nAMAUSAHALineEdit.setObjectName(u"nAMAUSAHALineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nAMAUSAHALineEdit)

        self.lOKASILabel = QLabel(Form)
        self.lOKASILabel.setObjectName(u"lOKASILabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lOKASILabel)

        self.lOKASILineEdit = QLineEdit(Form)
        self.lOKASILineEdit.setObjectName(u"lOKASILineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lOKASILineEdit)

        self.tAHUNBERDIRILabel = QLabel(Form)
        self.tAHUNBERDIRILabel.setObjectName(u"tAHUNBERDIRILabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tAHUNBERDIRILabel)

        self.tAHUNBERDIRISpinBox = QSpinBox(Form)
        self.tAHUNBERDIRISpinBox.setObjectName(u"tAHUNBERDIRISpinBox")
        self.tAHUNBERDIRISpinBox.setMinimum(1900)
        self.tAHUNBERDIRISpinBox.setMaximum(2100)
        self.tAHUNBERDIRISpinBox.setValue(2025)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tAHUNBERDIRISpinBox)

        self.jUMLAHBURUHLabel = QLabel(Form)
        self.jUMLAHBURUHLabel.setObjectName(u"jUMLAHBURUHLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jUMLAHBURUHLabel)

        self.jUMLAHBURUHSpinBox = QSpinBox(Form)
        self.jUMLAHBURUHSpinBox.setObjectName(u"jUMLAHBURUHSpinBox")
        self.jUMLAHBURUHSpinBox.setMaximum(1000000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.jUMLAHBURUHSpinBox)

        self.pENDAPATANLabel = QLabel(Form)
        self.pENDAPATANLabel.setObjectName(u"pENDAPATANLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.pENDAPATANLabel)

        self.pENDAPATANLineEdit = QLineEdit(Form)
        self.pENDAPATANLineEdit.setObjectName(u"pENDAPATANLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.pENDAPATANLineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayoutButtons = QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName(u"horizontalLayoutButtons")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayoutButtons.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayoutButtons.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayoutButtons.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayoutButtons.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayoutButtons)

        self.EditCari = QLineEdit(Form)
        self.EditCari.setObjectName(u"EditCari")

        self.verticalLayout.addWidget(self.EditCari)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Usaha", None))
        self.iDUSAHALabel.setText(QCoreApplication.translate("Form", u"ID USAHA", None))
        self.nAMAUSAHALabel.setText(QCoreApplication.translate("Form", u"NAMA USAHA", None))
        self.lOKASILabel.setText(QCoreApplication.translate("Form", u"LOKASI", None))
        self.tAHUNBERDIRILabel.setText(QCoreApplication.translate("Form", u"TAHUN BERDIRI", None))
        self.jUMLAHBURUHLabel.setText(QCoreApplication.translate("Form", u"JUMLAH BURUH", None))
        self.pENDAPATANLabel.setText(QCoreApplication.translate("Form", u"PENDAPATAN", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_usaha", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nama_usaha", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"lokasi", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"tahun_berdiri", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"jumlah_buruh", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"pendapatan_bulanan", None));
    # retranslateUi

