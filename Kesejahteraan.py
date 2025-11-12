# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class Kesejahteraan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("Kesejahteraan.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formKesejahteraan = loader.load(ui_file, self)
        ui_file.close()

        # object CRUD (koneksi DB)
        self.crud = my_cruddb()
        self.formKesejahteraan.pushButton.clicked.connect(self.doSimpanKesejahteraan)
        self.formKesejahteraan.pushButton_4.clicked.connect(self.doUbahKesejahteraan)
        self.formKesejahteraan.pushButton_2.clicked.connect(self.doHapusKesejahteraan)
        self.formKesejahteraan.pushButton_3.clicked.connect(self.doBersihKesejahteraan)

        self.muatComboKeluarga()
        self.muatComboAdmin()

        self.tampilData()
        self.formKesejahteraan.EditCari.textChanged.connect(self.doCariKesejahteraan)

    def muatComboKeluarga(self):
        cb = self.formKesejahteraan.comboBox
        cb.clear()
        cb.addItem("— pilih keluarga —", None)
        for r in self.crud.listKeluarga():
            cb.addItem(f'{r["nama_kepala_keluarga"]} (ID: {r["id_keluarga"]})', r["id_keluarga"])

    def muatComboAdmin(self):
        cb = self.formKesejahteraan.comboBox_2
        cb.clear()
        cb.addItem("— pilih admin —", None)
        for r in self.crud.listAdmin():
            cb.addItem(f'{r["username"]} (ID: {r["id_admin"]})', r["id_admin"])

    def doSimpanKesejahteraan(self):
        if self.formKesejahteraan.comboBox.currentData() is None:
            QMessageBox.information(None, "Informasi", "ID Keluarga belum dipilih")
            self.formKesejahteraan.comboBox.setFocus()
        elif self.formKesejahteraan.tAHUNSpinBox.value() <= 0:
            QMessageBox.information(None, "Informasi", "Tahun belum valid")
            self.formKesejahteraan.tAHUNSpinBox.setFocus()
        elif not self.formKesejahteraan.pENGHASILANBLNLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Penghasilan belum di isi")
            self.formKesejahteraan.pENGHASILANBLNLineEdit.setFocus()
        elif not self.formKesejahteraan.pENDIDIKANANAKLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Pendidikan Anak belum di isi")
            self.formKesejahteraan.pENDIDIKANANAKLineEdit.setFocus()
        elif not self.formKesejahteraan.sTATUSRUMAHComboBox.currentText().strip():
            QMessageBox.information(None, "Informasi", "Status Rumah belum di isi")
            self.formKesejahteraan.sTATUSRUMAHComboBox.setFocus()
        elif not self.formKesejahteraan.kATEGORIIPMComboBox.currentText().strip():
            QMessageBox.information(None, "Informasi", "Kategori IPM belum di isi")
            self.formKesejahteraan.kATEGORIIPMComboBox.setFocus()
        elif self.formKesejahteraan.comboBox_2.currentData() is None:
            QMessageBox.information(None, "Informasi", "Dibuat Oleh belum dipilih")
            self.formKesejahteraan.comboBox_2.setFocus()
        else:
            pesan = QMessageBox.information(
                None,
                "Informasi",
                "Apakah Anda Yakin Menyimpan Data Ini?",
                QMessageBox.Yes | QMessageBox.No
            )
            if pesan == QMessageBox.Yes:
                tempIDKeluarga     = self.formKesejahteraan.comboBox.currentData()
                tempTahun          = self.formKesejahteraan.tAHUNSpinBox.value()
                tempPenghasilan    = self.formKesejahteraan.pENGHASILANBLNLineEdit.text()
                tempPendidikanAnak = self.formKesejahteraan.pENDIDIKANANAKLineEdit.text()
                tempStatusRumah    = self.formKesejahteraan.sTATUSRUMAHComboBox.currentText()
                tempKategoriIPM    = self.formKesejahteraan.kATEGORIIPMComboBox.currentText()
                tempDibuatOleh     = self.formKesejahteraan.comboBox_2.currentData()

                self.crud.simpanKesejahteraan(
                    tempIDKeluarga,
                    tempTahun,
                    tempPenghasilan,
                    tempPendidikanAnak,
                    tempStatusRumah,
                    tempKategoriIPM,
                    tempDibuatOleh
                )
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")
            else:
                pass

    def doUbahKesejahteraan(self):
        tempIDKeluarga     = self.formKesejahteraan.comboBox.currentData()
        tempTahun          = self.formKesejahteraan.tAHUNSpinBox.value()
        tempPenghasilan    = self.formKesejahteraan.pENGHASILANBLNLineEdit.text()
        tempPendidikanAnak = self.formKesejahteraan.pENDIDIKANANAKLineEdit.text()
        tempStatusRumah    = self.formKesejahteraan.sTATUSRUMAHComboBox.currentText()
        tempKategoriIPM    = self.formKesejahteraan.kATEGORIIPMComboBox.currentText()
        tempDibuatOleh     = self.formKesejahteraan.comboBox_2.currentData()

        self.crud.ubahKesejahteraan(
            tempIDKeluarga,
            tempTahun,
            tempPenghasilan,
            tempPendidikanAnak,
            tempStatusRumah,
            tempKategoriIPM,
            tempDibuatOleh
        )
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def doHapusKesejahteraan(self):
        tempIDKeluarga = self.formKesejahteraan.comboBox.currentData()
        tempTahun      = self.formKesejahteraan.tAHUNSpinBox.value()

        self.crud.hapusKesejahteraan(tempIDKeluarga, tempTahun)
        QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    def doBersihKesejahteraan(self):
        self.formKesejahteraan.comboBox.setCurrentIndex(0)
        self.formKesejahteraan.tAHUNSpinBox.setValue(2025)
        self.formKesejahteraan.pENGHASILANBLNLineEdit.clear()
        self.formKesejahteraan.pENDIDIKANANAKLineEdit.clear()
        self.formKesejahteraan.sTATUSRUMAHComboBox.setCurrentIndex(0)
        self.formKesejahteraan.kATEGORIIPMComboBox.setCurrentIndex(0)
        self.formKesejahteraan.comboBox_2.setCurrentIndex(0)

    def tampilData(self):
        baris = self.crud.dataKesejahteraan()
        self.formKesejahteraan.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formKesejahteraan.tableWidget.rowCount()
            self.formKesejahteraan.tableWidget.insertRow(i)
            self.formKesejahteraan.tableWidget.setItem(i, 0, QTableWidgetItem(str(r["id_kesejahteraan"])))
            self.formKesejahteraan.tableWidget.setItem(i, 1, QTableWidgetItem("" if r["id_keluarga"] is None else str(r["id_keluarga"])))
            self.formKesejahteraan.tableWidget.setItem(i, 2, QTableWidgetItem(str(r["tahun"])))
            self.formKesejahteraan.tableWidget.setItem(i, 3, QTableWidgetItem("" if r["penghasilan"] is None else f"{float(r['penghasilan']):.2f}"))
            self.formKesejahteraan.tableWidget.setItem(i, 4, QTableWidgetItem(r["pendidikan_anak"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 5, QTableWidgetItem(r["status_rumah"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 6, QTableWidgetItem(r["kategori_ipm"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 7, QTableWidgetItem("" if r["dibuat_oleh"] is None else str(r["dibuat_oleh"])))

    def doCariKesejahteraan(self):
        cari = self.formKesejahteraan.EditCari.text()
        baris = self.crud.CariKesejahteraan(cari)
        self.formKesejahteraan.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formKesejahteraan.tableWidget.rowCount()
            self.formKesejahteraan.tableWidget.insertRow(i)
            self.formKesejahteraan.tableWidget.setItem(i, 0, QTableWidgetItem(str(r["id_kesejahteraan"])))
            self.formKesejahteraan.tableWidget.setItem(i, 1, QTableWidgetItem("" if r["id_keluarga"] is None else str(r["id_keluarga"])))
            self.formKesejahteraan.tableWidget.setItem(i, 2, QTableWidgetItem(str(r["tahun"])))
            self.formKesejahteraan.tableWidget.setItem(i, 3, QTableWidgetItem("" if r["penghasilan"] is None else f"{float(r['penghasilan']):.2f}"))
            self.formKesejahteraan.tableWidget.setItem(i, 4, QTableWidgetItem(r["pendidikan_anak"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 5, QTableWidgetItem(r["status_rumah"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 6, QTableWidgetItem(r["kategori_ipm"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 7, QTableWidgetItem("" if r["dibuat_oleh"] is None else str(r["dibuat_oleh"])))
