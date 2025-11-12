# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class DataKeluarga(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("DataKeluarga.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formKeluarga = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()
        self.formKeluarga.pushButton.clicked.connect(self.doSimpanKeluarga)
        self.formKeluarga.pushButton_4.clicked.connect(self.doUbahKeluarga)
        self.formKeluarga.pushButton_2.clicked.connect(self.doHapusKeluarga)
        self.formKeluarga.pushButton_3.clicked.connect(self.doBersihKeluarga)

        # isi combobox FK (id_usaha & dibuat_oleh)
        self.muatComboUsaha()
        self.muatComboAdmin()

        self.tampilData()
        self.formKeluarga.EditCari.textChanged.connect(self.doCariKeluarga)

    def muatComboUsaha(self):
        cb = self.formKeluarga.iDUSAHAComboBox
        cb.clear()
        cb.addItem("— pilih usaha —", None)
        for r in self.crud.listUsaha():
            cb.addItem(f'{r["nama_usaha"]} (ID: {r["id_usaha"]})', r["id_usaha"])

    def muatComboAdmin(self):
        cb = self.formKeluarga.dIBUATOLEHComboBox
        cb.clear()
        cb.addItem("— pilih admin —", None)
        for r in self.crud.listAdmin():
            cb.addItem(f'{r["username"]} (ID: {r["id_admin"]})', r["id_admin"])

    def doSimpanKeluarga(self):
        if not self.formKeluarga.nAMAKEPALAKELUARGALineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Kepala Keluarga belum di isi")
            self.formKeluarga.nAMAKEPALAKELUARGALineEdit.setFocus()
        elif not self.formKeluarga.aLAMATLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Alamat belum di isi")
            self.formKeluarga.aLAMATLineEdit.setFocus()
        elif self.formKeluarga.jUMLAHANGGOTASpinBox.value() <= 0:
            QMessageBox.information(None, "Informasi", "Jumlah Anggota belum valid")
            self.formKeluarga.jUMLAHANGGOTASpinBox.setFocus()
        elif not self.formKeluarga.sTATUSEKONOMIComboBox.currentText().strip():
            QMessageBox.information(None, "Informasi", "Status Ekonomi belum di isi")
            self.formKeluarga.sTATUSEKONOMIComboBox.setFocus()
        elif self.formKeluarga.iDUSAHAComboBox.currentData() is None:
            QMessageBox.information(None, "Informasi", "ID Usaha belum dipilih")
            self.formKeluarga.iDUSAHAComboBox.setFocus()
        elif self.formKeluarga.dIBUATOLEHComboBox.currentData() is None:
            QMessageBox.information(None, "Informasi", "Dibuat Oleh belum dipilih")
            self.formKeluarga.dIBUATOLEHComboBox.setFocus()
        else:
            pesan = QMessageBox.information(
                None,
                "Informasi",
                "Apakah Anda Yakin Menyimpan Data Ini?",
                QMessageBox.Yes | QMessageBox.No
            )
            if pesan == QMessageBox.Yes:
                tempNamaKK     = self.formKeluarga.nAMAKEPALAKELUARGALineEdit.text()
                tempAlamat     = self.formKeluarga.aLAMATLineEdit.text()
                tempJumlah     = self.formKeluarga.jUMLAHANGGOTASpinBox.value()
                tempStatus     = self.formKeluarga.sTATUSEKONOMIComboBox.currentText()
                tempIDUsaha    = self.formKeluarga.iDUSAHAComboBox.currentData()
                tempDibuatOleh = self.formKeluarga.dIBUATOLEHComboBox.currentData()

                self.crud.simpanKeluarga(
                    tempNamaKK, tempAlamat, tempJumlah,
                    tempStatus, tempIDUsaha, tempDibuatOleh
                )
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")

    def doUbahKeluarga(self):
        tempIDKel      = self.formKeluarga.iDKELUARGALineEdit.text()
        tempNamaKK     = self.formKeluarga.nAMAKEPALAKELUARGALineEdit.text()
        tempAlamat     = self.formKeluarga.aLAMATLineEdit.text()
        tempJumlah     = self.formKeluarga.jUMLAHANGGOTASpinBox.value()
        tempStatus     = self.formKeluarga.sTATUSEKONOMIComboBox.currentText()
        tempIDUsaha    = self.formKeluarga.iDUSAHAComboBox.currentData()
        tempDibuatOleh = self.formKeluarga.dIBUATOLEHComboBox.currentData()

        self.crud.ubahKeluarga(
            tempIDKel, tempNamaKK, tempAlamat, tempJumlah,
            tempStatus, tempIDUsaha, tempDibuatOleh
        )
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def doHapusKeluarga(self):
        tempIDKel = self.formKeluarga.iDKELUARGALineEdit.text()
        self.crud.hapusKeluarga(tempIDKel)
        QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    def doBersihKeluarga(self):
        self.formKeluarga.iDKELUARGALineEdit.clear()
        self.formKeluarga.nAMAKEPALAKELUARGALineEdit.clear()
        self.formKeluarga.aLAMATLineEdit.clear()
        self.formKeluarga.jUMLAHANGGOTASpinBox.setValue(0)
        self.formKeluarga.sTATUSEKONOMIComboBox.setCurrentIndex(0)
        self.formKeluarga.iDUSAHAComboBox.setCurrentIndex(0)
        self.formKeluarga.dIBUATOLEHComboBox.setCurrentIndex(0)

    def tampilData(self):
        baris = self.crud.dataKeluarga()
        print(baris)
        self.formKeluarga.tabelKeluarga.setRowCount(0)
        for r in baris:
            i = self.formKeluarga.tabelKeluarga.rowCount()
            self.formKeluarga.tabelKeluarga.insertRow(i)
            self.formKeluarga.tabelKeluarga.setItem(i, 0, QTableWidgetItem(str(r["id_keluarga"])))
            self.formKeluarga.tabelKeluarga.setItem(i, 1, QTableWidgetItem(r["nama_kepala_keluarga"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 2, QTableWidgetItem(r["alamat"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 3, QTableWidgetItem(str(r["jumlah_anggota"]) if r["jumlah_anggota"] is not None else ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 4, QTableWidgetItem(r["status_ekonomi"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 5, QTableWidgetItem(str(r["id_usaha"]) if r["id_usaha"] is not None else ""))

    def doCariKeluarga(self):
        cari = self.formKeluarga.EditCari.text()
        baris = self.crud.CariKeluarga(cari)
        self.formKeluarga.tabelKeluarga.setRowCount(0)
        for r in baris:
            i = self.formKeluarga.tabelKeluarga.rowCount()
            self.formKeluarga.tabelKeluarga.insertRow(i)
            self.formKeluarga.tabelKeluarga.setItem(i, 0, QTableWidgetItem(str(r["id_keluarga"])))
            self.formKeluarga.tabelKeluarga.setItem(i, 1, QTableWidgetItem(r["nama_kepala_keluarga"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 2, QTableWidgetItem(r["alamat"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 3, QTableWidgetItem(str(r["jumlah_anggota"]) if r["jumlah_anggota"] is not None else ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 4, QTableWidgetItem(r["status_ekonomi"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 5, QTableWidgetItem(str(r["id_usaha"]) if r["id_usaha"] is not None else ""))
