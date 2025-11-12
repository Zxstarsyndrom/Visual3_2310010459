# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class DataUsaha(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("DataUsaha.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formUsaha = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()
        self.formUsaha.pushButton.clicked.connect(self.doSimpanUsaha)
        self.formUsaha.pushButton_4.clicked.connect(self.doUbahUsaha)
        self.formUsaha.pushButton_2.clicked.connect(self.doHapusUsaha)
        self.formUsaha.pushButton_3.clicked.connect(self.doBersihUsaha)
        self.tampilData()
        self.formUsaha.EditCari.textChanged.connect(self.doCariUsaha)

    def doSimpanUsaha(self):
        if not self.formUsaha.nAMAUSAHALineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Usaha belum di isi")
            self.formUsaha.nAMAUSAHALineEdit.setFocus()
        elif not self.formUsaha.lOKASILineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Lokasi belum di isi")
            self.formUsaha.lOKASILineEdit.setFocus()
        elif not self.formUsaha.pENDAPATANLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Pendapatan Bulanan belum di isi")
            self.formUsaha.pENDAPATANLineEdit.setFocus()
        else:
            pesan = QMessageBox.information(
                None,
                "Informasi",
                "Apakah Anda Yakin Menyimpan Data Ini?",
                QMessageBox.Yes | QMessageBox.No
            )
            if pesan == QMessageBox.Yes:
                tempNamaUsaha    = self.formUsaha.nAMAUSAHALineEdit.text()
                tempLokasi       = self.formUsaha.lOKASILineEdit.text()
                tempTahunBerdiri = self.formUsaha.tAHUNBERDIRISpinBox.value()
                tempJumlahBuruh  = self.formUsaha.jUMLAHBURUHSpinBox.value()
                tempPendapatan   = self.formUsaha.pENDAPATANLineEdit.text()

                self.crud.simpanUsaha(
                    tempNamaUsaha,
                    tempLokasi,
                    tempTahunBerdiri,
                    tempJumlahBuruh,
                    tempPendapatan
                )
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")

    def doUbahUsaha(self):
        tempIDUsaha      = self.formUsaha.iDUSAHALineEdit.text()
        tempNamaUsaha    = self.formUsaha.nAMAUSAHALineEdit.text()
        tempLokasi       = self.formUsaha.lOKASILineEdit.text()
        tempTahunBerdiri = self.formUsaha.tAHUNBERDIRISpinBox.value()
        tempJumlahBuruh  = self.formUsaha.jUMLAHBURUHSpinBox.value()
        tempPendapatan   = self.formUsaha.pENDAPATANLineEdit.text()

        self.crud.ubahUsaha(
            tempIDUsaha,
            tempNamaUsaha,
            tempLokasi,
            tempTahunBerdiri,
            tempJumlahBuruh,
            tempPendapatan
        )
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def doHapusUsaha(self):
        tempIDUsaha = self.formUsaha.iDUSAHALineEdit.text()
        self.crud.hapusUsaha(tempIDUsaha)
        QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    def doBersihUsaha(self):
        self.formUsaha.iDUSAHALineEdit.clear()
        self.formUsaha.nAMAUSAHALineEdit.clear()
        self.formUsaha.lOKASILineEdit.clear()
        self.formUsaha.tAHUNBERDIRISpinBox.setValue(2025)
        self.formUsaha.jUMLAHBURUHSpinBox.setValue(0)
        self.formUsaha.pENDAPATANLineEdit.clear()

    def tampilData(self):
        baris = self.crud.dataUsaha()
        print(baris)
        self.formUsaha.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formUsaha.tableWidget.rowCount()
            self.formUsaha.tableWidget.insertRow(i)
            self.formUsaha.tableWidget.setItem(i, 0, QTableWidgetItem(r["nama_usaha"] if r["nama_usaha"] is not None else ""))
            self.formUsaha.tableWidget.setItem(i, 1, QTableWidgetItem(str(r["id_usaha"])))
            self.formUsaha.tableWidget.setItem(i, 2, QTableWidgetItem(r["lokasi"] if r["lokasi"] is not None else ""))
            self.formUsaha.tableWidget.setItem(i, 3, QTableWidgetItem(str(r["tahun_berdiri"]) if r["tahun_berdiri"] is not None else ""))
            self.formUsaha.tableWidget.setItem(i, 4, QTableWidgetItem(str(r["jumlah_buruh"]) if r["jumlah_buruh"] is not None else ""))
            self.formUsaha.tableWidget.setItem(i, 5, QTableWidgetItem(str(r["pendapatan_bulanan"]) if r["pendapatan_bulanan"] is not None else ""))

    def doCariUsaha(self):
        cari = self.formUsaha.EditCari.text()
        baris = self.crud.CariUsaha(cari)
        self.formUsaha.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formUsaha.tableWidget.rowCount()
            self.formUsaha.tableWidget.insertRow(i)
            self.formUsaha.tableWidget.setItem(i, 0, QTableWidgetItem(r["nama_usaha"] if r["nama_usaha"] is not None else ""))
            self.formUsaha.tableWidget.setItem(i, 1, QTableWidgetItem(str(r["id_usaha"])))
            self.formUsaha.tableWidget.setItem(i, 2, QTableWidgetItem(r["lokasi"] if r["lokasi"] is not None else ""))
            self.formUsaha.tableWidget.setItem(i, 3, QTableWidgetItem(str(r["tahun_berdiri"]) if r["tahun_berdiri"] is not None else ""))
            self.formUsaha.tableWidget.setItem(i, 4, QTableWidgetItem(str(r["jumlah_buruh"]) if r["jumlah_buruh"] is not None else ""))
            self.formUsaha.tableWidget.setItem(i, 5, QTableWidgetItem(str(r["pendapatan_bulanan"]) if r["pendapatan_bulanan"] is not None else ""))
