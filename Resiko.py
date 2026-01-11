# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb

class Resiko(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Loading UI File
        ui_file = QFile("Resiko.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formResiko = loader.load(ui_file, self)
        ui_file.close()

        # 2. Object CRUD (Koneksi Database)
        self.crud = my_cruddb()

        # 3. Koneksi Tombol CRUD
        self.formResiko.pushButton.clicked.connect(self.doSimpanResiko)    # Simpan
        self.formResiko.pushButton_4.clicked.connect(self.doUbahResiko)   # Ubah
        self.formResiko.pushButton_2.clicked.connect(self.doHapusResiko)  # Hapus
        self.formResiko.pushButton_3.clicked.connect(self.doBersihResiko) # Bersih

        # 4. Koneksi Tabel (Signal Klik) & Pencarian
        self.formResiko.tableWidget.cellClicked.connect(self.getData)     # Ambil data saat klik
        self.formResiko.EditCari.textChanged.connect(self.doCariResiko)   # Search real-time

        # 5. Inisialisasi Data Awal
        self.muatComboPekerja()
        self.muatComboAdmin()
        self.setupTable()
        self.tampilData()

    def getData(self, row, col):
        """Mengambil data dari baris tabel ke dalam form input"""
        # Mapping Kolom sesuai setupTable
        item_id_pekerja = self.formResiko.tableWidget.item(row, 0) # ID Pekerja
        item_jenis      = self.formResiko.tableWidget.item(row, 1) # Jenis Risiko
        item_tingkat    = self.formResiko.tableWidget.item(row, 2) # Tingkat
        item_tindakan   = self.formResiko.tableWidget.item(row, 3) # Tindakan Pencegahan
        item_tanggal    = self.formResiko.tableWidget.item(row, 4) # Tanggal Insiden
        item_admin      = self.formResiko.tableWidget.item(row, 5) # Dibuat Oleh

        # Isi LineEdit
        if item_jenis:
            self.formResiko.jENISRESIKOLineEdit.setText(item_jenis.text())
        if item_tindakan:
            self.formResiko.tINDAKANPENCEGAHANLineEdit.setText(item_tindakan.text())

        # Isi DateEdit (Konversi string database ke QDate)
        if item_tanggal:
            date_obj = QDate.fromString(item_tanggal.text(), "yyyy-MM-dd")
            self.formResiko.tANGGALINSIDENDateEdit.setDate(date_obj)

        # Isi ComboBox Tingkat Risiko (Teks Enum)
        if item_tingkat:
            self.formResiko.comboBox.setCurrentText(item_tingkat.text())

        # Isi ComboBox Foreign Key (Mencari berdasarkan ID)
        if item_id_pekerja:
            idx_p = self.formResiko.comboBox_2.findData(int(item_id_pekerja.text()))
            self.formResiko.comboBox_2.setCurrentIndex(idx_p)

        if item_admin:
            idx_a = self.formResiko.comboBox_3.findData(int(item_admin.text()))
            self.formResiko.comboBox_3.setCurrentIndex(idx_a)

    def setupTable(self):
        tbl = self.formResiko.tableWidget
        tbl.setColumnCount(6)
        tbl.setHorizontalHeaderLabels([
            "ID Pekerja", "Jenis Risiko", "Tingkat", "Tindakan Pencegahan",
            "Tanggal Insiden", "Dibuat Oleh"
        ])
        tbl.horizontalHeader().setStretchLastSection(True)

    def muatComboPekerja(self):
        cb = self.formResiko.comboBox_2
        cb.clear()
        cb.addItem("— pilih pekerja —", None)
        for r in self.crud.listPekerja():
            cb.addItem(f'{r["nama_pekerja"]} (ID: {r["id_pekerja"]})', r["id_pekerja"])

    def muatComboAdmin(self):
        cb = self.formResiko.comboBox_3
        cb.clear()
        cb.addItem("— pilih admin —", None)
        for r in self.crud.listAdmin():
            cb.addItem(f'{r["username"]} (ID: {r["id_admin"]})', r["id_admin"])

    def doSimpanResiko(self):
        if self.formResiko.comboBox_2.currentData() is None:
            QMessageBox.information(self, "Informasi", "ID Pekerja belum dipilih")
            self.formResiko.comboBox_2.setFocus()
        elif not self.formResiko.jENISRESIKOLineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Jenis Risiko belum di isi")
            self.formResiko.jENISRESIKOLineEdit.setFocus()
        else:
            pesan = QMessageBox.question(self, "Konfirmasi", "Simpan data risiko ini?",
                                         QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                self.crud.simpanResiko(
                    self.formResiko.comboBox_2.currentData(),
                    self.formResiko.jENISRESIKOLineEdit.text(),
                    self.formResiko.comboBox.currentText().strip().lower(),
                    self.formResiko.tINDAKANPENCEGAHANLineEdit.text(),
                    self.formResiko.tANGGALINSIDENDateEdit.date().toString("yyyy-MM-dd"),
                    self.formResiko.comboBox_3.currentData()
                )
                self.tampilData()
                self.doBersihResiko()
                QMessageBox.information(self, "Informasi", "Data Berhasil Disimpan")

    def doUbahResiko(self):
        if self.formResiko.comboBox_2.currentData() is None:
            QMessageBox.warning(self, "Peringatan", "Pilih data di tabel terlebih dahulu!")
            return

        self.crud.ubahResiko(
            self.formResiko.comboBox_2.currentData(),
            self.formResiko.jENISRESIKOLineEdit.text(),
            self.formResiko.comboBox.currentText().strip().lower(),
            self.formResiko.tINDAKANPENCEGAHANLineEdit.text(),
            self.formResiko.tANGGALINSIDENDateEdit.date().toString("yyyy-MM-dd"),
            self.formResiko.comboBox_3.currentData()
        )
        self.tampilData()
        QMessageBox.information(self, "Informasi", "Data berhasil diubah")

    def doHapusResiko(self):
        id_p = self.formResiko.comboBox_2.currentData()
        jenis = self.formResiko.jENISRESIKOLineEdit.text()
        tgl = self.formResiko.tANGGALINSIDENDateEdit.date().toString("yyyy-MM-dd")

        if id_p is None:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan dihapus!")
            return

        pesan = QMessageBox.question(self, "Konfirmasi", f"Yakin hapus risiko Pekerja ID {id_p}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            self.crud.hapusResiko(id_p, jenis, tgl)
            self.tampilData()
            self.doBersihResiko()
            QMessageBox.information(self, "Informasi", "Data berhasil dihapus")

    def doBersihResiko(self):
        self.formResiko.comboBox_2.setCurrentIndex(0)
        self.formResiko.jENISRESIKOLineEdit.clear()
        self.formResiko.comboBox.setCurrentIndex(0)
        self.formResiko.tINDAKANPENCEGAHANLineEdit.clear()
        self.formResiko.comboBox_3.setCurrentIndex(0)
        self.formResiko.tANGGALINSIDENDateEdit.setDate(QDate.currentDate())

    def tampilData(self):
        rows = self.crud.dataResiko()
        tbl = self.formResiko.tableWidget
        tbl.setRowCount(0)
        for r in rows:
            i = tbl.rowCount()
            tbl.insertRow(i)
            tbl.setItem(i, 0, QTableWidgetItem(str(r.get("id_pekerja", ""))))
            tbl.setItem(i, 1, QTableWidgetItem(r.get("jenis_risiko") or ""))
            tbl.setItem(i, 2, QTableWidgetItem(r.get("tingkat_risiko") or ""))
            tbl.setItem(i, 3, QTableWidgetItem(r.get("tindakan_pencegahan") or ""))
            tbl.setItem(i, 4, QTableWidgetItem(str(r.get("tanggal_insiden", ""))))
            tbl.setItem(i, 5, QTableWidgetItem(str(r.get("dibuat_oleh", ""))))

    def doCariResiko(self):
        cari = self.formResiko.EditCari.text()
        baris = self.crud.CariResiko(cari)
        tbl = self.formResiko.tableWidget
        tbl.setRowCount(0)
        for r in baris:
            i = tbl.rowCount()
            tbl.insertRow(i)
            tbl.setItem(i, 0, QTableWidgetItem(str(r.get("id_pekerja", ""))))
            tbl.setItem(i, 1, QTableWidgetItem(r.get("jenis_risiko") or ""))
            tbl.setItem(i, 2, QTableWidgetItem(r.get("tingkat_risiko") or ""))
            tbl.setItem(i, 3, QTableWidgetItem(r.get("tindakan_pencegahan") or ""))
            tbl.setItem(i, 4, QTableWidgetItem(str(r.get("tanggal_insiden", ""))))
            tbl.setItem(i, 5, QTableWidgetItem(str(r.get("dibuat_oleh", ""))))
