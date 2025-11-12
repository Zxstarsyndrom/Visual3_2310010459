# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataKeluarga.ui'
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
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(628, 578)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nAMAKEPALAKELUARGALabel = QLabel(Form)
        self.nAMAKEPALAKELUARGALabel.setObjectName(u"nAMAKEPALAKELUARGALabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nAMAKEPALAKELUARGALabel)

        self.nAMAKEPALAKELUARGALineEdit = QLineEdit(Form)
        self.nAMAKEPALAKELUARGALineEdit.setObjectName(u"nAMAKEPALAKELUARGALineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nAMAKEPALAKELUARGALineEdit)

        self.aLAMATLabel = QLabel(Form)
        self.aLAMATLabel.setObjectName(u"aLAMATLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.aLAMATLabel)

        self.aLAMATLineEdit = QLineEdit(Form)
        self.aLAMATLineEdit.setObjectName(u"aLAMATLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.aLAMATLineEdit)

        self.jUMLAHANGGOTALabel = QLabel(Form)
        self.jUMLAHANGGOTALabel.setObjectName(u"jUMLAHANGGOTALabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jUMLAHANGGOTALabel)

        self.jUMLAHANGGOTASpinBox = QSpinBox(Form)
        self.jUMLAHANGGOTASpinBox.setObjectName(u"jUMLAHANGGOTASpinBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.jUMLAHANGGOTASpinBox)

        self.sTATUSEKONOMILabel = QLabel(Form)
        self.sTATUSEKONOMILabel.setObjectName(u"sTATUSEKONOMILabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.sTATUSEKONOMILabel)

        self.sTATUSEKONOMIComboBox = QComboBox(Form)
        self.sTATUSEKONOMIComboBox.addItem("")
        self.sTATUSEKONOMIComboBox.addItem("")
        self.sTATUSEKONOMIComboBox.addItem("")
        self.sTATUSEKONOMIComboBox.setObjectName(u"sTATUSEKONOMIComboBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.sTATUSEKONOMIComboBox)

        self.iDUSAHALabel = QLabel(Form)
        self.iDUSAHALabel.setObjectName(u"iDUSAHALabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.iDUSAHALabel)

        self.iDUSAHAComboBox = QComboBox(Form)
        self.iDUSAHAComboBox.setObjectName(u"iDUSAHAComboBox")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.iDUSAHAComboBox)

        self.dIBUATOLEHLabel = QLabel(Form)
        self.dIBUATOLEHLabel.setObjectName(u"dIBUATOLEHLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.dIBUATOLEHLabel)

        self.dIBUATOLEHComboBox = QComboBox(Form)
        self.dIBUATOLEHComboBox.setObjectName(u"dIBUATOLEHComboBox")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.dIBUATOLEHComboBox)


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

        self.tabelKeluarga = QTableWidget(Form)
        if (self.tabelKeluarga.columnCount() < 6):
            self.tabelKeluarga.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelKeluarga.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelKeluarga.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelKeluarga.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelKeluarga.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelKeluarga.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabelKeluarga.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabelKeluarga.setObjectName(u"tabelKeluarga")

        self.verticalLayout.addWidget(self.tabelKeluarga)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nAMAKEPALAKELUARGALabel.setText(QCoreApplication.translate("Form", u"NAMA KEPALA KELUARGA", None))
        self.aLAMATLabel.setText(QCoreApplication.translate("Form", u"ALAMAT", None))
        self.jUMLAHANGGOTALabel.setText(QCoreApplication.translate("Form", u"JUMLAH ANGGOTA", None))
        self.sTATUSEKONOMILabel.setText(QCoreApplication.translate("Form", u"STATUS EKONOMI", None))
        self.sTATUSEKONOMIComboBox.setItemText(0, QCoreApplication.translate("Form", u"sejahtera bawah", None))
        self.sTATUSEKONOMIComboBox.setItemText(1, QCoreApplication.translate("Form", u"sejahtera menengah", None))
        self.sTATUSEKONOMIComboBox.setItemText(2, QCoreApplication.translate("Form", u"sejahtera atas", None))

        self.iDUSAHALabel.setText(QCoreApplication.translate("Form", u"ID USAHA", None))
        self.dIBUATOLEHLabel.setText(QCoreApplication.translate("Form", u"DIBUAT OLEH", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tabelKeluarga.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_keluarga", None));
        ___qtablewidgetitem1 = self.tabelKeluarga.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nama_kepala_keluarga", None));
        ___qtablewidgetitem2 = self.tabelKeluarga.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"alamat", None));
        ___qtablewidgetitem3 = self.tabelKeluarga.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"jumlah_anggota", None));
        ___qtablewidgetitem4 = self.tabelKeluarga.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"status_ekonomi", None));
        ___qtablewidgetitem5 = self.tabelKeluarga.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"id_Usaha", None));
    # retranslateUi

