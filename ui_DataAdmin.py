# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataAdmin.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(464, 603)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.iDADMINLabel = QLabel(Form)
        self.iDADMINLabel.setObjectName(u"iDADMINLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDADMINLabel)

        self.iDADMINLineEdit = QLineEdit(Form)
        self.iDADMINLineEdit.setObjectName(u"iDADMINLineEdit")
        self.iDADMINLineEdit.setReadOnly(False)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.iDADMINLineEdit)

        self.uSERNAMELabel = QLabel(Form)
        self.uSERNAMELabel.setObjectName(u"uSERNAMELabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.uSERNAMELabel)

        self.uSERNAMELineEdit = QLineEdit(Form)
        self.uSERNAMELineEdit.setObjectName(u"uSERNAMELineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.uSERNAMELineEdit)

        self.pASSWORDLabel = QLabel(Form)
        self.pASSWORDLabel.setObjectName(u"pASSWORDLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.pASSWORDLabel)

        self.pASSWORDLineEdit = QLineEdit(Form)
        self.pASSWORDLineEdit.setObjectName(u"pASSWORDLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.pASSWORDLineEdit)

        self.nAMALabel = QLabel(Form)
        self.nAMALabel.setObjectName(u"nAMALabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.nAMALabel)

        self.nAMALineEdit = QLineEdit(Form)
        self.nAMALineEdit.setObjectName(u"nAMALineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.nAMALineEdit)

        self.eMAILLabel = QLabel(Form)
        self.eMAILLabel.setObjectName(u"eMAILLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.eMAILLabel)

        self.eMAILLineEdit = QLineEdit(Form)
        self.eMAILLineEdit.setObjectName(u"eMAILLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.eMAILLineEdit)

        self.rOLELabel = QLabel(Form)
        self.rOLELabel.setObjectName(u"rOLELabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.rOLELabel)

        self.rOLEComboBox = QComboBox(Form)
        self.rOLEComboBox.addItem("")
        self.rOLEComboBox.addItem("")
        self.rOLEComboBox.setObjectName(u"rOLEComboBox")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.rOLEComboBox)

        self.tANGGALDIBUATLabel = QLabel(Form)
        self.tANGGALDIBUATLabel.setObjectName(u"tANGGALDIBUATLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.tANGGALDIBUATLabel)

        self.tANGGALDIBUATLineEdit = QLineEdit(Form)
        self.tANGGALDIBUATLineEdit.setObjectName(u"tANGGALDIBUATLineEdit")
        self.tANGGALDIBUATLineEdit.setReadOnly(True)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.tANGGALDIBUATLineEdit)


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
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDADMINLabel.setText(QCoreApplication.translate("Form", u"ID ADMIN", None))
        self.uSERNAMELabel.setText(QCoreApplication.translate("Form", u"USERNAME", None))
        self.pASSWORDLabel.setText(QCoreApplication.translate("Form", u"PASSWORD", None))
        self.nAMALabel.setText(QCoreApplication.translate("Form", u"NAMA", None))
        self.eMAILLabel.setText(QCoreApplication.translate("Form", u"EMAIL", None))
        self.rOLELabel.setText(QCoreApplication.translate("Form", u"ROLE", None))
        self.rOLEComboBox.setItemText(0, QCoreApplication.translate("Form", u"admin", None))
        self.rOLEComboBox.setItemText(1, QCoreApplication.translate("Form", u"staff", None))

        self.tANGGALDIBUATLabel.setText(QCoreApplication.translate("Form", u"TANGGAL DIBUAT", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_admin", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"username", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"password", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"nama_lengkap", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"email", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"role", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"tanggal_dibuat", None));
    # retranslateUi

