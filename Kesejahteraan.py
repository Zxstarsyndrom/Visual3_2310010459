# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class Kesejahteraan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Loading UI File
        ui_file = QFile("Kesejahteraan.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formKesejahteraan = loader.load(ui_file, self)
        ui_file.close()

        # 2. Object CRUD (Koneksi Database)
        self.crud = my_cruddb()

        # 3. Koneksi Tombol CRUD
        self.formKesejahteraan.pushButton.clicked.connect(self.doSimpanKesejahteraan)   # Simpan
        self.formKesejahteraan.pushButton_4.clicked.connect(self.doUbahKesejahteraan)  # Ubah
        self.formKesejahteraan.pushButton_2.clicked.connect(self.doHapusKesejahteraan) # Hapus
        self.formKesejahteraan.pushButton_3.clicked.connect(self.doBersihKesejahteraan) # Bersih

        # 4. Koneksi Tabel (Signal Klik) & Pencarian
        self.formKesejahteraan.tableWidget.cellClicked.connect(self.getData)           # Ambil data saat klik
        self.formKesejahteraan.EditCari.textChanged.connect(self.doCariKesejahteraan)  # Search real-time

        # 5. Inisialisasi Data Awal
        self.muatComboKeluarga()
        self.muatComboAdmin()
        self.tampilData()

    def getData(self, row, col):
        """Mengambil data dari baris tabel yang diklik dan menampilkannya di form input"""
        # Mapping Kolom Tabel (berdasarkan urutan di tampilData)
        item_id_kel      = self.formKesejahteraan.tableWidget.item(row, 1) # Kolom 1: ID Keluarga
        item_tahun       = self.formKesejahteraan.tableWidget.item(row, 2) # Kolom 2: Tahun
        item_penghasilan = self.formKesejahteraan.tableWidget.item(row, 3) # Kolom 3: Penghasilan
        item_pendidikan  = self.formKesejahteraan.tableWidget.item(row, 4) # Kolom 4: Pendidikan Anak
        item_rumah       = self.formKesejahteraan.tableWidget.item(row, 5) # Kolom 5: Status Rumah
        item_ipm         = self.formKesejahteraan.tableWidget.item(row, 6) # Kolom 6: Kategori IPM
        item_admin       = self.formKesejahteraan.tableWidget.item(row, 7) # Kolom 7: Dibuat Oleh (Admin)

        # Isi LineEdit
        if item_penghasilan: self.formKesejahteraan.pENGHASILANBLNLineEdit.setText(item_penghasilan.text())
        if item_pendidikan: self.formKesejahteraan.pENDIDIKANANAKLineEdit.setText(item_pendidikan.text())

        # Isi SpinBox (Tahun)
        if item_tahun:
            self.formKesejahteraan.tAHUNSpinBox.setValue(int(item_tahun.text()))

        # Isi ComboBox Status & IPM (Teks)
        if item_rumah:
            self.formKesejahteraan.sTATUSRUMAHComboBox.setCurrentText(item_rumah.text())
        if item_ipm:
            self.formKesejahteraan.kATEGORIIPMComboBox.setCurrentText(item_ipm.text())

        # Isi ComboBox Foreign Key (Mencari berdasarkan ID di data item)
        if item_id_kel:
            idx_kel = self.formKesejahteraan.comboBox.findData(int(item_id_kel.text()))
            self.formKesejahteraan.comboBox.setCurrentIndex(idx_kel)

        if item_admin:
            idx_adm = self.formKesejahteraan.comboBox_2.findData(int(item_admin.text()))
            self.formKesejahteraan.comboBox_2.setCurrentIndex(idx_adm)

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
            QMessageBox.information(self, "Informasi", "ID Keluarga belum dipilih")
            self.formKesejahteraan.comboBox.setFocus()
        elif not self.formKesejahteraan.pENGHASILANBLNLineEdit.text().strip():
            QMessageBox.information(self, "Informasi", "Penghasilan belum di isi")
            self.formKesejahteraan.pENGHASILANBLNLineEdit.setFocus()
        else:
            pesan = QMessageBox.question(self, "Konfirmasi", "Apakah Anda Yakin Menyimpan Data Ini?",
                                         QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                self.crud.simpanKesejahteraan(
                    self.formKesejahteraan.comboBox.currentData(),
                    self.formKesejahteraan.tAHUNSpinBox.value(),
                    self.formKesejahteraan.pENGHASILANBLNLineEdit.text(),
                    self.formKesejahteraan.pENDIDIKANANAKLineEdit.text(),
                    self.formKesejahteraan.sTATUSRUMAHComboBox.currentText(),
                    self.formKesejahteraan.kATEGORIIPMComboBox.currentText(),
                    self.formKesejahteraan.comboBox_2.currentData()
                )
                self.tampilData()
                self.doBersihKesejahteraan()
                QMessageBox.information(self, "Informasi", "Data Berhasil Disimpan")

    def doUbahKesejahteraan(self):
        # Memeriksa apakah data sudah dipilih (biasanya via ID Keluarga & Tahun)
        if self.formKesejahteraan.comboBox.currentData() is None:
            QMessageBox.warning(self, "Peringatan", "Pilih data di tabel terlebih dahulu!")
            return

        self.crud.ubahKesejahteraan(
            self.formKesejahteraan.comboBox.currentData(),
            self.formKesejahteraan.tAHUNSpinBox.value(),
            self.formKesejahteraan.pENGHASILANBLNLineEdit.text(),
            self.formKesejahteraan.pENDIDIKANANAKLineEdit.text(),
            self.formKesejahteraan.sTATUSRUMAHComboBox.currentText(),
            self.formKesejahteraan.kATEGORIIPMComboBox.currentText(),
            self.formKesejahteraan.comboBox_2.currentData()
        )
        self.tampilData()
        QMessageBox.information(self, "Informasi", "Data berhasil diubah")

    def doHapusKesejahteraan(self):
        id_kel = self.formKesejahteraan.comboBox.currentData()
        tahun = self.formKesejahteraan.tAHUNSpinBox.value()

        if id_kel is None:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan dihapus!")
            return

        pesan = QMessageBox.question(self, "Konfirmasi", f"Yakin hapus data Kesejahteraan Keluarga ID {id_kel} Tahun {tahun}?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            self.crud.hapusKesejahteraan(id_kel, tahun)
            self.tampilData()
            self.doBersihKesejahteraan()
            QMessageBox.information(self, "Informasi", "Data berhasil dihapus")

    def doBersihKesejahteraan(self):
        self.formKesejahteraan.comboBox.setCurrentIndex(0)
        self.formKesejahteraan.tAHUNSpinBox.setValue(2026) # Update ke tahun berjalan
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

            penghasilan = r.get("penghasilan")
            p_text = "" if penghasilan is None else f"{float(penghasilan):.2f}"
            self.formKesejahteraan.tableWidget.setItem(i, 3, QTableWidgetItem(p_text))

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

            penghasilan = r.get("penghasilan")
            p_text = "" if penghasilan is None else f"{float(penghasilan):.2f}"
            self.formKesejahteraan.tableWidget.setItem(i, 3, QTableWidgetItem(p_text))

            self.formKesejahteraan.tableWidget.setItem(i, 4, QTableWidgetItem(r["pendidikan_anak"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 5, QTableWidgetItem(r["status_rumah"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 6, QTableWidgetItem(r["kategori_ipm"] or ""))
            self.formKesejahteraan.tableWidget.setItem(i, 7, QTableWidgetItem("" if r["dibuat_oleh"] is None else str(r["dibuat_oleh"])))
