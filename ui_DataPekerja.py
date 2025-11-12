# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataPekerja.ui'
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
        Form.resize(495, 600)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nAMAPEKERJALabel = QLabel(Form)
        self.nAMAPEKERJALabel.setObjectName(u"nAMAPEKERJALabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nAMAPEKERJALabel)

        self.nAMAPEKERJALineEdit = QLineEdit(Form)
        self.nAMAPEKERJALineEdit.setObjectName(u"nAMAPEKERJALineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nAMAPEKERJALineEdit)

        self.jENISKELAMINLabel = QLabel(Form)
        self.jENISKELAMINLabel.setObjectName(u"jENISKELAMINLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.jENISKELAMINLabel)

        self.jENISKELAMINComboBox = QComboBox(Form)
        self.jENISKELAMINComboBox.addItem("")
        self.jENISKELAMINComboBox.addItem("")
        self.jENISKELAMINComboBox.setObjectName(u"jENISKELAMINComboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.jENISKELAMINComboBox)

        self.pEKERJAANLabel = QLabel(Form)
        self.pEKERJAANLabel.setObjectName(u"pEKERJAANLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.pEKERJAANLabel)

        self.pEKERJAANLineEdit = QLineEdit(Form)
        self.pEKERJAANLineEdit.setObjectName(u"pEKERJAANLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.pEKERJAANLineEdit)

        self.iDUSAHALabel = QLabel(Form)
        self.iDUSAHALabel.setObjectName(u"iDUSAHALabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.iDUSAHALabel)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.iDKELUARGALabel = QLabel(Form)
        self.iDKELUARGALabel.setObjectName(u"iDKELUARGALabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.iDKELUARGALabel)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboBox_2)

        self.dIBUATOLEHLabel = QLabel(Form)
        self.dIBUATOLEHLabel.setObjectName(u"dIBUATOLEHLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.dIBUATOLEHLabel)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.comboBox_3)

        self.gajiLineEdit = QLineEdit(Form)
        self.gajiLineEdit.setObjectName(u"gajiLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.gajiLineEdit)

        self.gajiLabel = QLabel(Form)
        self.gajiLabel.setObjectName(u"gajiLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.gajiLabel)


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
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Data Usaha", None))
        self.nAMAPEKERJALabel.setText(QCoreApplication.translate("Form", u"NAMA PEKERJA", None))
        self.jENISKELAMINLabel.setText(QCoreApplication.translate("Form", u"JENIS KELAMIN", None))
        self.jENISKELAMINComboBox.setItemText(0, QCoreApplication.translate("Form", u"Laki-laki", None))
        self.jENISKELAMINComboBox.setItemText(1, QCoreApplication.translate("Form", u"Perempuan", None))

        self.pEKERJAANLabel.setText(QCoreApplication.translate("Form", u"PEKERJAAN", None))
        self.iDUSAHALabel.setText(QCoreApplication.translate("Form", u"ID USAHA", None))
        self.iDKELUARGALabel.setText(QCoreApplication.translate("Form", u"ID KELUARGA", None))
        self.dIBUATOLEHLabel.setText(QCoreApplication.translate("Form", u"DIBUAT OLEH", None))
        self.gajiLabel.setText(QCoreApplication.translate("Form", u"Gaji", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"BERSIH", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"UBAH", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id_pekerja", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nama_pekerja", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"jenis_kelamin", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"pekerjaan", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"gaji", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"id_usaha", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"id_keluarga", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"dibuat_oleh", None));
    # retranslateUi

