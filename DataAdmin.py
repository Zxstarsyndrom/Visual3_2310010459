# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class DataAdmin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file = QFile("DataAdmin.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formAdmin = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()
        self.formAdmin.pushButton.clicked.connect(self.doSimpanAdmin)
        self.formAdmin.pushButton_4.clicked.connect(self.doUbahAdmin)
        self.formAdmin.pushButton_2.clicked.connect(self.doHapusAdmin)
        self.formAdmin.pushButton_3.clicked.connect(self.doBersihAdmin)
        self.tampilData()
        self.formAdmin.EditCari.textChanged.connect(self.doCariAdmin)

    def doSimpanAdmin(self):
        if not self.formAdmin.uSERNAMELineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Username belum di isi")
            self.formAdmin.uSERNAMELineEdit.setFocus()
        elif not self.formAdmin.pASSWORDLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Password belum di isi")
            self.formAdmin.pASSWORDLineEdit.setFocus()
        elif not self.formAdmin.nAMALineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Admin belum di isi")
            self.formAdmin.nAMALineEdit.setFocus()
        elif not self.formAdmin.eMAILLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Email belum di isi")
            self.formAdmin.eMAILLineEdit.setFocus()
        elif not self.formAdmin.rOLEComboBox.currentText().strip():
            QMessageBox.information(None, "Informasi", "Role belum di isi")
            self.formAdmin.rOLEComboBox.setFocus()
        else:
            pesan = QMessageBox.information(
                None,
                "Informasi",
                "Apakah Anda Yakin Menyimpan Data Ini?",
                QMessageBox.Yes | QMessageBox.No
            )
            if pesan == QMessageBox.Yes:
                tempUsername = self.formAdmin.uSERNAMELineEdit.text()
                tempPassword = self.formAdmin.pASSWORDLineEdit.text()
                tempNama     = self.formAdmin.nAMALineEdit.text()
                tempEmail    = self.formAdmin.eMAILLineEdit.text()
                tempRole     = self.formAdmin.rOLEComboBox.currentText()
                self.crud.simpanAdmin(tempUsername, tempPassword, tempNama, tempEmail, tempRole)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")
            else:
                pass

    def doUbahAdmin(self):
        tempID       = self.formAdmin.iDADMINLineEdit.text()
        tempUsername = self.formAdmin.uSERNAMELineEdit.text()
        tempPassword = self.formAdmin.pASSWORDLineEdit.text()
        tempNama     = self.formAdmin.nAMALineEdit.text()
        tempEmail    = self.formAdmin.eMAILLineEdit.text()
        tempRole     = self.formAdmin.rOLEComboBox.currentText()
        self.crud.ubahAdmin(tempID, tempUsername, tempPassword, tempNama, tempEmail, tempRole)
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def doHapusAdmin(self):
        tempID = self.formAdmin.iDADMINLineEdit.text()
        self.crud.hapusAdmin(tempID)
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    def doBersihAdmin(self):
        self.formAdmin.iDADMINLineEdit.clear()
        self.formAdmin.uSERNAMELineEdit.clear()
        self.formAdmin.pASSWORDLineEdit.clear()
        self.formAdmin.nAMALineEdit.clear()
        self.formAdmin.eMAILLineEdit.clear()
        self.formAdmin.rOLEComboBox.setCurrentIndex(0)
        self.formAdmin.tANGGALDIBUATLineEdit.clear()

    def tampilData(self):
        baris = self.crud.dataAdmin()
        print(baris)
        self.formAdmin.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formAdmin.tableWidget.rowCount()
            self.formAdmin.tableWidget.insertRow(i)
            self.formAdmin.tableWidget.setItem(i, 0, QTableWidgetItem(str(r["id_admin"])))
            self.formAdmin.tableWidget.setItem(i, 1, QTableWidgetItem(r["username"] or ""))
            self.formAdmin.tableWidget.setItem(i, 2, QTableWidgetItem(r["password"] or ""))
            self.formAdmin.tableWidget.setItem(i, 3, QTableWidgetItem(r["nama_lengkap"] or ""))
            self.formAdmin.tableWidget.setItem(i, 4, QTableWidgetItem(r["email"] or ""))
            self.formAdmin.tableWidget.setItem(i, 5, QTableWidgetItem(r["role"] or ""))
            self.formAdmin.tableWidget.setItem(i, 6, QTableWidgetItem(str(r["tanggal_dibuat"]) if r["tanggal_dibuat"] else ""))

    def doCariAdmin(self):
        cari = self.formAdmin.EditCari.text()
        baris = self.crud.CariAdmin(cari)
        self.formAdmin.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formAdmin.tableWidget.rowCount()
            self.formAdmin.tableWidget.insertRow(i)
            self.formAdmin.tableWidget.setItem(i, 0, QTableWidgetItem(str(r["id_admin"])))
            self.formAdmin.tableWidget.setItem(i, 1, QTableWidgetItem(r["username"]))
            self.formAdmin.tableWidget.setItem(i, 2, QTableWidgetItem(r["password"]))
            self.formAdmin.tableWidget.setItem(i, 3, QTableWidgetItem(r["nama_lengkap"]))
            self.formAdmin.tableWidget.setItem(i, 4, QTableWidgetItem(r["email"]))
            self.formAdmin.tableWidget.setItem(i, 5, QTableWidgetItem(r["role"]))
            self.formAdmin.tableWidget.setItem(i, 6, QTableWidgetItem(str(r["tanggal_dibuat"]) if r["tanggal_dibuat"] else ""))
