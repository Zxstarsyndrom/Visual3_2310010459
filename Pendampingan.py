# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb

class Pendampingan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Loading UI File
        ui_file = QFile("Pendampingan.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPendampingan = loader.load(ui_file, self)
        ui_file.close()

        # 2. Object CRUD (Koneksi Database)
        self.crud = my_cruddb()

        # 3. Koneksi Tombol CRUD
        self.formPendampingan.pushButton.clicked.connect(self.doSimpanPendampingan)   # Simpan
        self.formPendampingan.pushButton_4.clicked.connect(self.doUbahPendampingan)  # Ubah
        self.formPendampingan.pushButton_2.clicked.connect(self.doHapusPendampingan) # Hapus
        self.formPendampingan.pushButton_3.clicked.connect(self.doBersihPendampingan) # Bersih

        # 4. Koneksi Tabel (Signal Klik) & Pencarian
        self.formPendampingan.tableWidget.cellClicked.connect(self.getData)           # Ambil data saat klik
        self.formPendampingan.EditCari.textChanged.connect(self.doCariPendampingan)  # Search real-time

        # 5. Inisialisasi Data Awal
        self.muatComboUsaha()
        self.muatComboAdmin()
        self.tampilData()

    def getData(self, row, col):
        """Memindahkan data dari tabel ke form input saat baris diklik"""
        # Mapping Kolom sesuai urutan di tampilData
        item_nama       = self.formPendampingan.tableWidget.item(row, 1) # Kolom 1: Nama Program
        item_mulai      = self.formPendampingan.tableWidget.item(row, 2) # Kolom 2: Tanggal Mulai
        item_selesai    = self.formPendampingan.tableWidget.item(row, 3) # Kolom 3: Tanggal Selesai
        item_lembaga    = self.formPendampingan.tableWidget.item(row, 4) # Kolom 4: Lembaga
        item_id_usaha   = self.formPendampingan.tableWidget.item(row, 5) # Kolom 5: ID Usaha
        item_admin      = self.formPendampingan.tableWidget.item(row, 6) # Kolom 6: Dibuat Oleh

        # Isi LineEdit
        if item_nama: self.formPendampingan.nAMAPROGRAMLineEdit.setText(item_nama.text())
        if item_lembaga: self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.setText(item_lembaga.text())

        # Isi DateEdit (Konversi string database ke QDate)
        if item_mulai:
            date_m = QDate.fromString(item_mulai.text(), "yyyy-MM-dd")
            self.formPendampingan.tANGGALSELESAIDateEdit.setDate(date_m)
        if item_selesai:
            date_s = QDate.fromString(item_selesai.text(), "yyyy-MM-dd")
            self.formPendampingan.tANGGALSELESAIDateEdit_2.setDate(date_s)

        # Isi ComboBox Foreign Key (Mencari berdasarkan ID di data item)
        if item_id_usaha:
            idx_u = self.formPendampingan.comboBox.findData(int(item_id_usaha.text()))
            self.formPendampingan.comboBox.setCurrentIndex(idx_u)

        if item_admin:
            idx_a = self.formPendampingan.comboBox_2.findData(int(item_admin.text()))
            self.formPendampingan.comboBox_2.setCurrentIndex(idx_a)

    def muatComboUsaha(self):
        cb = self.formPendampingan.comboBox
        cb.clear() # Perbaikan: Tambah tanda kurung ()
        cb.addItem("— pilih usaha —", None)
        for r in self.crud.listUsaha():
            cb.addItem(f'{r["nama_usaha"]} (ID: {r["id_usaha"]})', r["id_usaha"])

    def muatComboAdmin(self):
        cb = self.formPendampingan.comboBox_2
        cb.clear()
        cb.addItem("— pilih admin —", None)
        for r in self.crud.listAdmin():
            cb.addItem(f'{r["username"]} (ID: {r["id_admin"]})', r["id_admin"])

    def doSimpanPendampingan(self):
        if not self.formPendampingan.nAMAPROGRAMLineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Nama Program belum di isi")
            self.formPendampingan.nAMAPROGRAMLineEdit.setFocus()
        elif self.formPendampingan.comboBox.currentData() is None:
            QMessageBox.information(self, "Informasi", "ID Usaha belum dipilih")
            self.formPendampingan.comboBox.setFocus()
        else:
            pesan = QMessageBox.question(self, "Konfirmasi", "Apakah Anda Yakin Menyimpan Data Ini?",
                                         QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                self.crud.simpanPendampingan(
                    self.formPendampingan.nAMAPROGRAMLineEdit.text(),
                    self.formPendampingan.tANGGALSELESAIDateEdit.date().toString("yyyy-MM-dd"),
                    self.formPendampingan.tANGGALSELESAIDateEdit_2.date().toString("yyyy-MM-dd"),
                    self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.text(),
                    self.formPendampingan.comboBox.currentData(),
                    self.formPendampingan.comboBox_2.currentData()
                )
                self.tampilData()
                self.doBersihPendampingan()
                QMessageBox.information(self, "Informasi", "Data Berhasil Disimpan")

    def doUbahPendampingan(self):
        # Validasi sederhana sebelum ubah
        if not self.formPendampingan.nAMAPROGRAMLineEdit.text().strip():
            QMessageBox.warning(self, "Peringatan", "Pilih data di tabel terlebih dahulu!")
            return

        self.crud.ubahPendampingan(
            self.formPendampingan.nAMAPROGRAMLineEdit.text(),
            self.formPendampingan.tANGGALSELESAIDateEdit.date().toString("yyyy-MM-dd"),
            self.formPendampingan.tANGGALSELESAIDateEdit_2.date().toString("yyyy-MM-dd"),
            self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.text(),
            self.formPendampingan.comboBox.currentData(),
            self.formPendampingan.comboBox_2.currentData()
        )
        self.tampilData()
        QMessageBox.information(self, "Informasi", "Data berhasil diubah")

    def doHapusPendampingan(self):
        nama_prog = self.formPendampingan.nAMAPROGRAMLineEdit.text()
        if not nama_prog:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan dihapus!")
            return

        pesan = QMessageBox.question(self, "Konfirmasi", f"Yakin hapus program: {nama_prog}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            self.crud.hapusPendampingan(nama_prog)
            self.tampilData()
            self.doBersihPendampingan()
            QMessageBox.information(self, "Informasi", "Data berhasil dihapus")

    def doBersihPendampingan(self):
        self.formPendampingan.nAMAPROGRAMLineEdit.clear()
        self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.clear()
        self.formPendampingan.comboBox.setCurrentIndex(0)
        self.formPendampingan.comboBox_2.setCurrentIndex(0)
        self.formPendampingan.tANGGALSELESAIDateEdit.setDate(QDate.currentDate())
        self.formPendampingan.tANGGALSELESAIDateEdit_2.setDate(QDate.currentDate())

    def tampilData(self):
        baris = self.crud.dataPendampingan()
        self.formPendampingan.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formPendampingan.tableWidget.rowCount()
            self.formPendampingan.tableWidget.insertRow(i)
            self.formPendampingan.tableWidget.setItem(i, 0, QTableWidgetItem(str(r.get("id_pendampingan", ""))))
            self.formPendampingan.tableWidget.setItem(i, 1, QTableWidgetItem(r.get("nama_program") or ""))
            self.formPendampingan.tableWidget.setItem(i, 2, QTableWidgetItem(str(r.get("tanggal_mulai", ""))))
            self.formPendampingan.tableWidget.setItem(i, 3, QTableWidgetItem(str(r.get("tanggal_selesai", ""))))
            self.formPendampingan.tableWidget.setItem(i, 4, QTableWidgetItem(r.get("lembaga_pendamping") or ""))
            self.formPendampingan.tableWidget.setItem(i, 5, QTableWidgetItem(str(r.get("id_usaha", ""))))
            self.formPendampingan.tableWidget.setItem(i, 6, QTableWidgetItem(str(r.get("dibuat_oleh", ""))))

    def doCariPendampingan(self):
        cari = self.formPendampingan.EditCari.text()
        baris = self.crud.CariPendampingan(cari)
        self.formPendampingan.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formPendampingan.tableWidget.rowCount()
            self.formPendampingan.tableWidget.insertRow(i)
            self.formPendampingan.tableWidget.setItem(i, 0, QTableWidgetItem(str(r.get("id_pendampingan", ""))))
            self.formPendampingan.tableWidget.setItem(i, 1, QTableWidgetItem(r.get("nama_program") or ""))
            self.formPendampingan.tableWidget.setItem(i, 2, QTableWidgetItem(str(r.get("tanggal_mulai", ""))))
            self.formPendampingan.tableWidget.setItem(i, 3, QTableWidgetItem(str(r.get("tanggal_selesai", ""))))
            self.formPendampingan.tableWidget.setItem(i, 4, QTableWidgetItem(r.get("lembaga_pendamping") or ""))
            self.formPendampingan.tableWidget.setItem(i, 5, QTableWidgetItem(str(r.get("id_usaha", ""))))
            self.formPendampingan.tableWidget.setItem(i, 6, QTableWidgetItem(str(r.get("dibuat_oleh", ""))))
