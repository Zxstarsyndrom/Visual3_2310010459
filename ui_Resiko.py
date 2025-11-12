# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Resiko.ui'
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
        Form.resize(489, 634)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.iDPEKERJALabel = QLabel(Form)
        self.iDPEKERJALabel.setObjectName(u"iDPEKERJALabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPEKERJALabel)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_2)

        self.jENISRESIKOLabel = QLabel(Form)
        self.jENISRESIKOLabel.setObjectName(u"jENISRESIKOLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.jENISRESIKOLabel)

        self.jENISRESIKOLineEdit = QLineEdit(Form)
        self.jENISRESIKOLineEdit.setObjectName(u"jENISRESIKOLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.jENISRESIKOLineEdit)

        self.tINGKATRESIKOLabel = QLabel(Form)
        self.tINGKATRESIKOLabel.setObjectName(u"tINGKATRESIKOLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tINGKATRESIKOLabel)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.tINDAKANPENCEGAHANLabel = QLabel(Form)
        self.tINDAKANPENCEGAHANLabel.setObjectName(u"tINDAKANPENCEGAHANLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tINDAKANPENCEGAHANLabel)

        self.tINDAKANPENCEGAHANLineEdit = QLineEdit(Form)
        self.tINDAKANPENCEGAHANLineEdit.setObjectName(u"tINDAKANPENCEGAHANLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tINDAKANPENCEGAHANLineEdit)

        self.tANGGALINSIDENLabel = QLabel(Form)
        self.tANGGALINSIDENLabel.setObjectName(u"tANGGALINSIDENLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tANGGALINSIDENLabel)

        self.tANGGALINSIDENDateEdit = QDateEdit(Form)
        self.tANGGALINSIDENDateEdit.setObjectName(u"tANGGALINSIDENDateEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tANGGALINSIDENDateEdit)

        self.dIBUATOLEHLabel = QLabel(Form)
        self.dIBUATOLEHLabel.setObjectName(u"dIBUATOLEHLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.dIBUATOLEHLabel)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboBox_3)


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
        self.iDPEKERJALabel.setText(QCoreApplication.translate("Form", u"ID PEKERJA", None))
        self.jENISRESIKOLabel.setText(QCoreApplication.translate("Form", u"JENIS RESIKO", None))
        self.tINGKATRESIKOLabel.setText(QCoreApplication.translate("Form", u"TINGKAT RESIKO", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Rendah", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Sedang", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Tinggi", None))

        self.tINDAKANPENCEGAHANLabel.setText(QCoreApplication.translate("Form", u"TINDAKAN PENCEGAHAN", None))
        self.tANGGALINSIDENLabel.setText(QCoreApplication.translate("Form", u"TANGGAL INSIDEN", None))
        self.dIBUATOLEHLabel.setText(QCoreApplication.translate("Form", u"DIBUAT OLEH", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_risiko", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"id_pekerja", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"jenis_risiko", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"tingkat_risiko", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"tindakan_pencegahan", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Tanggal_indisiden", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"dibuat_oleh", None));
    # retranslateUi

