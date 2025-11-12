# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pendampingan.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(495, 618)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nAMAPROGRAMLabel = QLabel(Form)
        self.nAMAPROGRAMLabel.setObjectName(u"nAMAPROGRAMLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nAMAPROGRAMLabel)

        self.nAMAPROGRAMLineEdit = QLineEdit(Form)
        self.nAMAPROGRAMLineEdit.setObjectName(u"nAMAPROGRAMLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nAMAPROGRAMLineEdit)

        self.tANGGALSELESAILabel = QLabel(Form)
        self.tANGGALSELESAILabel.setObjectName(u"tANGGALSELESAILabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.tANGGALSELESAILabel)

        self.tANGGALSELESAIDateEdit = QDateEdit(Form)
        self.tANGGALSELESAIDateEdit.setObjectName(u"tANGGALSELESAIDateEdit")
        self.tANGGALSELESAIDateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.tANGGALSELESAIDateEdit)

        self.tANGGALSELESAILabel_2 = QLabel(Form)
        self.tANGGALSELESAILabel_2.setObjectName(u"tANGGALSELESAILabel_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tANGGALSELESAILabel_2)

        self.tANGGALSELESAIDateEdit_2 = QDateEdit(Form)
        self.tANGGALSELESAIDateEdit_2.setObjectName(u"tANGGALSELESAIDateEdit_2")
        self.tANGGALSELESAIDateEdit_2.setCalendarPopup(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.tANGGALSELESAIDateEdit_2)

        self.lEMBAGAPENDAMPINGLabel = QLabel(Form)
        self.lEMBAGAPENDAMPINGLabel.setObjectName(u"lEMBAGAPENDAMPINGLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lEMBAGAPENDAMPINGLabel)

        self.lEMBAGAPENDAMPINGLineEdit = QLineEdit(Form)
        self.lEMBAGAPENDAMPINGLineEdit.setObjectName(u"lEMBAGAPENDAMPINGLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lEMBAGAPENDAMPINGLineEdit)

        self.iDUSAHALabel = QLabel(Form)
        self.iDUSAHALabel.setObjectName(u"iDUSAHALabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.iDUSAHALabel)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.dIBUATOLEHLabel = QLabel(Form)
        self.dIBUATOLEHLabel.setObjectName(u"dIBUATOLEHLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.dIBUATOLEHLabel)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboBox_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QHBoxLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.formLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.formLayout_2)

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

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nAMAPROGRAMLabel.setText(QCoreApplication.translate("Form", u"NAMA PROGRAM", None))
        self.tANGGALSELESAILabel.setText(QCoreApplication.translate("Form", u"TANGGAL MULAI", None))
        self.tANGGALSELESAILabel_2.setText(QCoreApplication.translate("Form", u"TANGGAL SELESAI", None))
        self.lEMBAGAPENDAMPINGLabel.setText(QCoreApplication.translate("Form", u"LEMBAGA PENDAMPING", None))
        self.iDUSAHALabel.setText(QCoreApplication.translate("Form", u"ID USAHA", None))
        self.dIBUATOLEHLabel.setText(QCoreApplication.translate("Form", u"DIBUAT OLEH", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"BERSIH ", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_pendampingan", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nama_program", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"tanggal_mulai", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"tanggal_selesai", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"lembaga_pendamping", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"id_usaha", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"dibuat_oleh", None));
    # retranslateUi

