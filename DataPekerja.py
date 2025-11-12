# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class DataPekerja(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("DataPekerja.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formPekerja = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.formPekerja.pushButton.clicked.connect(self.doSimpanPekerja)
        self.formPekerja.pushButton_4.clicked.connect(self.doUbahPekerja)
        self.formPekerja.pushButton_2.clicked.connect(self.doHapusPekerja)
        self.formPekerja.pushButton_3.clicked.connect(self.doBersihPekerja)

        self.muatComboUsaha()
        self.muatComboKeluarga()
        self.muatComboAdmin()

        self.tampilData()
        self.formPekerja.EditCari.textChanged.connect(self.doCariPekerja)

    def muatComboUsaha(self):
        cb = self.formPekerja.comboBox
        cb.clear()
        cb.addItem("— pilih usaha —", None)
        for r in self.crud.listUsaha():
            cb.addItem(f'{r["nama_usaha"]} (ID: {r["id_usaha"]})', r["id_usaha"])

    def muatComboKeluarga(self):
        cb = self.formPekerja.comboBox_2
        cb.clear()
        cb.addItem("— pilih keluarga —", None)
        for r in self.crud.listKeluarga():
            cb.addItem(f'{r["nama_kepala_keluarga"]} (ID: {r["id_keluarga"]})', r["id_keluarga"])

    def muatComboAdmin(self):
        cb = self.formPekerja.comboBox_3
        cb.clear()
        cb.addItem("— pilih admin —", None)
        for r in self.crud.listAdmin():
            cb.addItem(f'{r["username"]} (ID: {r["id_admin"]})', r["id_admin"])

    def doSimpanPekerja(self):
        if not self.formPekerja.nAMAPEKERJALineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Pekerja belum di isi")
            self.formPekerja.nAMAPEKERJALineEdit.setFocus()
        elif not self.formPekerja.jENISKELAMINComboBox.currentText().strip():
            QMessageBox.information(None, "Informasi", "Jenis Kelamin belum di isi")
            self.formPekerja.jENISKELAMINComboBox.setFocus()
        elif not self.formPekerja.pEKERJAANLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Pekerjaan belum di isi")
            self.formPekerja.pEKERJAANLineEdit.setFocus()
        elif not self.formPekerja.gajiLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Gaji belum di isi")
            self.formPekerja.gajiLineEdit.setFocus()
        elif self.formPekerja.comboBox.currentData() is None:
            QMessageBox.information(None, "Informasi", "ID Usaha belum dipilih")
            self.formPekerja.comboBox.setFocus()
        elif self.formPekerja.comboBox_2.currentData() is None:
            QMessageBox.information(None, "Informasi", "ID Keluarga belum dipilih")
            self.formPekerja.comboBox_2.setFocus()
        elif self.formPekerja.comboBox_3.currentData() is None:
            QMessageBox.information(None, "Informasi", "Dibuat Oleh belum dipilih")
            self.formPekerja.comboBox_3.setFocus()
        else:
            pesan = QMessageBox.information(
                None,
                "Informasi",
                "Apakah Anda Yakin Menyimpan Data Ini?",
                QMessageBox.Yes | QMessageBox.No
            )
            if pesan == QMessageBox.Yes:
                tempNamaPekerja  = self.formPekerja.nAMAPEKERJALineEdit.text()
                tempJenisKelamin = self.formPekerja.jENISKELAMINComboBox.currentText()
                tempPekerjaan    = self.formPekerja.pEKERJAANLineEdit.text()
                tempGaji         = self.formPekerja.gajiLineEdit.text()
                tempIDUsaha      = self.formPekerja.comboBox.currentData()
                tempIDKeluarga   = self.formPekerja.comboBox_2.currentData()
                tempDibuatOleh   = self.formPekerja.comboBox_3.currentData()

                self.crud.simpanPekerja(
                    tempNamaPekerja,
                    tempJenisKelamin,
                    tempPekerjaan,
                    tempGaji,
                    tempIDUsaha,
                    tempIDKeluarga,
                    tempDibuatOleh
                )
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")

    def doUbahPekerja(self):
        tempNamaPekerja  = self.formPekerja.nAMAPEKERJALineEdit.text()
        tempJenisKelamin = self.formPekerja.jENISKELAMINComboBox.currentText()
        tempPekerjaan    = self.formPekerja.pEKERJAANLineEdit.text()
        tempGaji         = self.formPekerja.gajiLineEdit.text()

        tempIDUsaha      = self.formPekerja.comboBox.currentData()
        tempIDKeluarga   = self.formPekerja.comboBox_2.currentData()
        tempDibuatOleh   = self.formPekerja.comboBox_3.currentData()

        self.crud.ubahPekerja(
            tempNamaPekerja,
            tempJenisKelamin,
            tempPekerjaan,
            tempGaji,
            tempIDUsaha,
            tempIDKeluarga,
            tempDibuatOleh
        )
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def doHapusPekerja(self):
        tempIDUsaha    = self.formPekerja.comboBox.currentData()
        tempIDKeluarga = self.formPekerja.comboBox_2.currentData()
        self.crud.hapusPekerja(tempIDUsaha, tempIDKeluarga)
        QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    def doBersihPekerja(self):
        self.formPekerja.nAMAPEKERJALineEdit.clear()
        self.formPekerja.pEKERJAANLineEdit.clear()
        self.formPekerja.gajiLineEdit.clear()
        self.formPekerja.jENISKELAMINComboBox.setCurrentIndex(0)
        self.formPekerja.comboBox.setCurrentIndex(0)
        self.formPekerja.comboBox_2.setCurrentIndex(0)
        self.formPekerja.comboBox_3.setCurrentIndex(0)

    def tampilData(self):
        baris = self.crud.dataPekerja()
        self.formPekerja.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formPekerja.tableWidget.rowCount()
            self.formPekerja.tableWidget.insertRow(i)

            self.formPekerja.tableWidget.setItem(
                i, 0, QTableWidgetItem("" if r.get("id_pekerja") is None else str(r["id_pekerja"]))
            )
            self.formPekerja.tableWidget.setItem(i, 1, QTableWidgetItem(r.get("nama_pekerja")  or ""))
            self.formPekerja.tableWidget.setItem(i, 2, QTableWidgetItem(r.get("jenis_kelamin") or ""))
            self.formPekerja.tableWidget.setItem(i, 3, QTableWidgetItem(r.get("pekerjaan")     or ""))

            gaji = r.get("gaji")
            gaji_text = "" if gaji is None else f"{gaji:.2f}"
            self.formPekerja.tableWidget.setItem(i, 4, QTableWidgetItem(gaji_text))

            self.formPekerja.tableWidget.setItem(
                i, 5, QTableWidgetItem("" if r.get("id_usaha")    is None else str(r["id_usaha"]))
            )
            self.formPekerja.tableWidget.setItem(
                i, 6, QTableWidgetItem("" if r.get("id_keluarga") is None else str(r["id_keluarga"]))
            )
            self.formPekerja.tableWidget.setItem(
                i, 7, QTableWidgetItem("" if r.get("dibuat_oleh") is None else str(r["dibuat_oleh"]))
            )

    def doCariPekerja(self):
        cari = self.formPekerja.EditCari.text()
        baris = self.crud.CariPekerja(cari)
        self.formPekerja.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formPekerja.tableWidget.rowCount()
            self.formPekerja.tableWidget.insertRow(i)

            self.formPekerja.tableWidget.setItem(i, 0, QTableWidgetItem(str(r["id_pekerja"])))
            self.formPekerja.tableWidget.setItem(i, 1, QTableWidgetItem(r["nama_pekerja"] or ""))
            self.formPekerja.tableWidget.setItem(i, 2, QTableWidgetItem(r["jenis_kelamin"] or ""))
            self.formPekerja.tableWidget.setItem(i, 3, QTableWidgetItem(r["pekerjaan"] or ""))

            gaji = r["gaji"]
            gaji_text = "" if gaji is None else f"{float(gaji):.2f}"
            self.formPekerja.tableWidget.setItem(i, 4, QTableWidgetItem(gaji_text))

            self.formPekerja.tableWidget.setItem(
                i, 5, QTableWidgetItem("" if r["id_usaha"]    is None else str(r["id_usaha"]))
            )
            self.formPekerja.tableWidget.setItem(
                i, 6, QTableWidgetItem("" if r["id_keluarga"] is None else str(r["id_keluarga"]))
            )
            self.formPekerja.tableWidget.setItem(
                i, 7, QTableWidgetItem("" if r["dibuat_oleh"] is None else str(r["dibuat_oleh"]))
            )
