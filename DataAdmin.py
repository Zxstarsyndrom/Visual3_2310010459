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
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formAdmin = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        # Koneksi Tombol
        self.formAdmin.pushButton.clicked.connect(self.doSimpanAdmin)     # Simpan
        self.formAdmin.pushButton_4.clicked.connect(self.doUbahAdmin)    # Ubah
        self.formAdmin.pushButton_2.clicked.connect(self.doHapusAdmin)   # Hapus
        self.formAdmin.pushButton_3.clicked.connect(self.doBersihAdmin)  # Bersih

        # Koneksi Tabel & Cari
        self.formAdmin.tableWidget.cellClicked.connect(self.getData)     # Ambil Data
        self.formAdmin.EditCari.textChanged.connect(self.doCariAdmin)    # Cari

        self.tampilData()

    def getData(self, row, col):
        """Mengambil data dari tabel ke dalam form input"""
        widgets = [
            self.formAdmin.iDADMINLineEdit,       # Kolom 0
            self.formAdmin.uSERNAMELineEdit,     # Kolom 1
            self.formAdmin.pASSWORDLineEdit,     # Kolom 2
            self.formAdmin.nAMALineEdit,         # Kolom 3
            self.formAdmin.eMAILLineEdit,        # Kolom 4
            self.formAdmin.rOLEComboBox,         # Kolom 5
            self.formAdmin.tANGGALDIBUATLineEdit # Kolom 6
        ]

        for index, widget in enumerate(widgets):
            item = self.formAdmin.tableWidget.item(row, index)
            if item:
                if hasattr(widget, 'setCurrentText'):
                    widget.setCurrentText(item.text())
                else:
                    widget.setText(item.text())

    def doSimpanAdmin(self):
        if not self.formAdmin.uSERNAMELineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Username belum di isi")
            self.formAdmin.uSERNAMELineEdit.setFocus()
        elif not self.formAdmin.pASSWORDLineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Password belum di isi")
            self.formAdmin.pASSWORDLineEdit.setFocus()
        elif not self.formAdmin.nAMALineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Nama Admin belum di isi")
            self.formAdmin.nAMALineEdit.setFocus()
        else:
            pesan = QMessageBox.question(self, "Konfirmasi", "Yakin simpan data?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                self.crud.simpanAdmin(
                    self.formAdmin.uSERNAMELineEdit.text(),
                    self.formAdmin.pASSWORDLineEdit.text(),
                    self.formAdmin.nAMALineEdit.text(),
                    self.formAdmin.eMAILLineEdit.text(),
                    self.formAdmin.rOLEComboBox.currentText()
                )
                self.tampilData()
                QMessageBox.information(self, "Informasi", "Data Berhasil di Simpan")

    def doUbahAdmin(self):
        tempID = self.formAdmin.iDADMINLineEdit.text()
        if not tempID:
            QMessageBox.warning(self, "Peringatan", "Pilih data di tabel dulu!")
            return

        self.crud.ubahAdmin(
            tempID,
            self.formAdmin.uSERNAMELineEdit.text(),
            self.formAdmin.pASSWORDLineEdit.text(),
            self.formAdmin.nAMALineEdit.text(),
            self.formAdmin.eMAILLineEdit.text(),
            self.formAdmin.rOLEComboBox.currentText()
        )
        self.tampilData()
        QMessageBox.information(self, "Informasi", "Data berhasil diubah")

    def doHapusAdmin(self):
        tempID = self.formAdmin.iDADMINLineEdit.text()
        if not tempID:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan dihapus!")
            return

        pesan = QMessageBox.question(self, "Konfirmasi", f"Hapus ID {tempID}?", QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            self.crud.hapusAdmin(tempID)
            self.tampilData()
            self.doBersihAdmin()
            QMessageBox.information(self, "Informasi", "Data berhasil dihapus")

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
            # Isi data hasil pencarian ke tabel (sama dengan tampilData)
            self.formAdmin.tableWidget.setItem(i, 0, QTableWidgetItem(str(r["id_admin"])))
            self.formAdmin.tableWidget.setItem(i, 1, QTableWidgetItem(r["username"]))
            self.formAdmin.tableWidget.setItem(i, 2, QTableWidgetItem(r["password"]))
            self.formAdmin.tableWidget.setItem(i, 3, QTableWidgetItem(r["nama_lengkap"]))
            self.formAdmin.tableWidget.setItem(i, 4, QTableWidgetItem(r["email"]))
            self.formAdmin.tableWidget.setItem(i, 5, QTableWidgetItem(r["role"]))
            self.formAdmin.tableWidget.setItem(i, 6, QTableWidgetItem(str(r["tanggal_dibuat"])))
