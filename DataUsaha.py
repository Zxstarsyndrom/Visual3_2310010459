# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class DataUsaha(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Loading UI File
        ui_file = QFile("DataUsaha.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formUsaha = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        # 2. Koneksi Tombol CRUD
        self.formUsaha.pushButton.clicked.connect(self.doSimpanUsaha)      # Tombol Simpan
        self.formUsaha.pushButton_4.clicked.connect(self.doUbahUsaha)     # Tombol Ubah
        self.formUsaha.pushButton_2.clicked.connect(self.doHapusUsaha)    # Tombol Hapus
        self.formUsaha.pushButton_3.clicked.connect(self.doBersihUsaha)   # Tombol Bersih

        # 3. Koneksi Tabel (Signal Klik) & Pencarian
        self.formUsaha.tableWidget.cellClicked.connect(self.getData)      # Ambil data saat klik
        self.formUsaha.EditCari.textChanged.connect(self.doCariUsaha)     # Real-time search

        # 4. Tampilkan Data Awal
        self.tampilData()

    def getData(self, row, col):
        """Memindahkan data dari tabel ke form input saat baris diklik"""
        # Mapping Kolom sesuai fungsi tampilData
        item_nama       = self.formUsaha.tableWidget.item(row, 0) # nama_usaha
        item_id         = self.formUsaha.tableWidget.item(row, 1) # id_usaha
        item_lokasi     = self.formUsaha.tableWidget.item(row, 2) # lokasi
        item_tahun      = self.formUsaha.tableWidget.item(row, 3) # tahun_berdiri
        item_buruh      = self.formUsaha.tableWidget.item(row, 4) # jumlah_buruh
        item_pendapatan = self.formUsaha.tableWidget.item(row, 5) # pendapatan_bulanan

        # Mengisi LineEdit
        if item_nama: self.formUsaha.nAMAUSAHALineEdit.setText(item_nama.text())
        if item_id: self.formUsaha.iDUSAHALineEdit.setText(item_id.text())
        if item_lokasi: self.formUsaha.lOKASILineEdit.setText(item_lokasi.text())
        if item_pendapatan: self.formUsaha.pENDAPATANLineEdit.setText(item_pendapatan.text())

        # Mengisi SpinBox (Tahun Berdiri & Jumlah Buruh)
        if item_tahun:
            self.formUsaha.tAHUNBERDIRISpinBox.setValue(int(item_tahun.text()))
        if item_buruh:
            self.formUsaha.jUMLAHBURUHSpinBox.setValue(int(item_buruh.text()))

    def doSimpanUsaha(self):
        """Validasi dan penyimpanan data usaha baru"""
        if not self.formUsaha.nAMAUSAHALineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Nama Usaha belum di isi")
            self.formUsaha.nAMAUSAHALineEdit.setFocus()
        elif not self.formUsaha.lOKASILineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Lokasi belum di isi")
            self.formUsaha.lOKASILineEdit.setFocus()
        elif not self.formUsaha.pENDAPATANLineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Pendapatan Bulanan belum di isi")
            self.formUsaha.pENDAPATANLineEdit.setFocus()
        else:
            pesan = QMessageBox.question(self, "Konfirmasi", "Apakah Anda Yakin Menyimpan Data Ini?",
                                         QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                self.crud.simpanUsaha(
                    self.formUsaha.nAMAUSAHALineEdit.text(),
                    self.formUsaha.lOKASILineEdit.text(),
                    self.formUsaha.tAHUNBERDIRISpinBox.value(),
                    self.formUsaha.jUMLAHBURUHSpinBox.value(),
                    self.formUsaha.pENDAPATANLineEdit.text()
                )
                self.tampilData()
                self.doBersihUsaha()
                QMessageBox.information(self, "Informasi", "Data Berhasil di Simpan")

    def doUbahUsaha(self):
        """Memperbarui data usaha yang dipilih"""
        tempIDUsaha = self.formUsaha.iDUSAHALineEdit.text()
        if not tempIDUsaha:
            QMessageBox.warning(self, "Peringatan", "Pilih data di tabel terlebih dahulu!")
            return

        self.crud.ubahUsaha(
            tempIDUsaha,
            self.formUsaha.nAMAUSAHALineEdit.text(),
            self.formUsaha.lOKASILineEdit.text(),
            self.formUsaha.tAHUNBERDIRISpinBox.value(),
            self.formUsaha.jUMLAHBURUHSpinBox.value(),
            self.formUsaha.pENDAPATANLineEdit.text()
        )
        self.tampilData()
        QMessageBox.information(self, "Informasi", "Data berhasil diubah")

    def doHapusUsaha(self):
        """Menghapus data usaha berdasarkan ID"""
        tempIDUsaha = self.formUsaha.iDUSAHALineEdit.text()
        if not tempIDUsaha:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan dihapus!")
            return

        pesan = QMessageBox.question(self, "Konfirmasi", f"Yakin hapus ID Usaha: {tempIDUsaha}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            self.crud.hapusUsaha(tempIDUsaha)
            self.tampilData()
            self.doBersihUsaha()
            QMessageBox.information(self, "Informasi", "Data berhasil dihapus")

    def doBersihUsaha(self):
        """Mengosongkan form input"""
        self.formUsaha.iDUSAHALineEdit.clear()
        self.formUsaha.nAMAUSAHALineEdit.clear()
        self.formUsaha.lOKASILineEdit.clear()
        self.formUsaha.tAHUNBERDIRISpinBox.setValue(2026) # Update ke tahun sekarang
        self.formUsaha.jUMLAHBURUHSpinBox.setValue(0)
        self.formUsaha.pENDAPATANLineEdit.clear()

    def tampilData(self):
        """Menampilkan seluruh data usaha ke tabel"""
        baris = self.crud.dataUsaha()
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
        """Melakukan pencarian data usaha secara real-time"""
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
