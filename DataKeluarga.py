# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class DataKeluarga(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Memuat File UI
        ui_file = QFile("DataKeluarga.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formKeluarga = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        # Variabel internal untuk menyimpan ID yang dipilih dari tabel
        self.id_terpilih = None

        # 2. Koneksi Tombol CRUD
        self.formKeluarga.pushButton.clicked.connect(self.doSimpanKeluarga)      # Simpan
        self.formKeluarga.pushButton_4.clicked.connect(self.doUbahKeluarga)     # Ubah
        self.formKeluarga.pushButton_2.clicked.connect(self.doHapusKeluarga)    # Hapus
        self.formKeluarga.pushButton_3.clicked.connect(self.doBersihKeluarga)   # Bersih

        # 3. Koneksi Tabel & Fitur Cari
        self.formKeluarga.tabelKeluarga.cellClicked.connect(self.getData)
        self.formKeluarga.EditCari.textChanged.connect(self.doCariKeluarga)

        # 4. Inisialisasi Data Awal
        self.muatComboUsaha()
        self.muatComboAdmin()
        self.tampilData()

    def getData(self, row, col):
        """Mengambil data dari tabel tanpa menampilkan ID ke widget"""
        # Ambil item dari kolom tabel (ID berada di kolom 0)
        item_id         = self.formKeluarga.tabelKeluarga.item(row, 0)
        item_nama_kk    = self.formKeluarga.tabelKeluarga.item(row, 1)
        item_alamat     = self.formKeluarga.tabelKeluarga.item(row, 2)
        item_jumlah     = self.formKeluarga.tabelKeluarga.item(row, 3)
        item_status     = self.formKeluarga.tabelKeluarga.item(row, 4)
        item_id_usaha   = self.formKeluarga.tabelKeluarga.item(row, 5)

        # Simpan ID ke variabel internal untuk proses Ubah/Hapus
        if item_id:
            self.id_terpilih = item_id.text()

        # Isi widget input lainnya yang ada di file UI
        if item_nama_kk: self.formKeluarga.nAMAKEPALAKELUARGALineEdit.setText(item_nama_kk.text())
        if item_alamat: self.formKeluarga.aLAMATLineEdit.setText(item_alamat.text())

        if item_jumlah:
            self.formKeluarga.jUMLAHANGGOTASpinBox.setValue(int(item_jumlah.text()))

        if item_status:
            self.formKeluarga.sTATUSEKONOMIComboBox.setCurrentText(item_status.text())

        if item_id_usaha:
            # Mencari index combo berdasarkan ID usaha
            idx = self.formKeluarga.iDUSAHAComboBox.findData(int(item_id_usaha.text()))
            self.formKeluarga.iDUSAHAComboBox.setCurrentIndex(idx)

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
        """Validasi dan simpan data baru"""
        if not self.formKeluarga.nAMAKEPALAKELUARGALineEdit.text().strip():
            QMessageBox.warning(self, "Peringatan", "Nama Kepala Keluarga wajib diisi!")
            return

        self.crud.simpanKeluarga(
            self.formKeluarga.nAMAKEPALAKELUARGALineEdit.text(),
            self.formKeluarga.aLAMATLineEdit.text(),
            self.formKeluarga.jUMLAHANGGOTASpinBox.value(),
            self.formKeluarga.sTATUSEKONOMIComboBox.currentText(),
            self.formKeluarga.iDUSAHAComboBox.currentData(),
            self.formKeluarga.dIBUATOLEHComboBox.currentData()
        )
        self.tampilData()
        self.doBersihKeluarga()
        QMessageBox.information(self, "Sukses", "Data keluarga berhasil disimpan!")

    def doUbahKeluarga(self):
        """Mengubah data berdasarkan ID yang tersimpan di memori"""
        if not self.id_terpilih:
            QMessageBox.warning(self, "Peringatan", "Klik data di tabel yang ingin diubah!")
            return

        self.crud.ubahKeluarga(
            self.id_terpilih,
            self.formKeluarga.nAMAKEPALAKELUARGALineEdit.text(),
            self.formKeluarga.aLAMATLineEdit.text(),
            self.formKeluarga.jUMLAHANGGOTASpinBox.value(),
            self.formKeluarga.sTATUSEKONOMIComboBox.currentText(),
            self.formKeluarga.iDUSAHAComboBox.currentData(),
            self.formKeluarga.dIBUATOLEHComboBox.currentData()
        )
        self.tampilData()
        QMessageBox.information(self, "Sukses", "Data berhasil diperbarui!")

    def doHapusKeluarga(self):
        """Menghapus data berdasarkan ID yang tersimpan di memori"""
        if not self.id_terpilih:
            QMessageBox.warning(self, "Peringatan", "Klik data di tabel yang ingin dihapus!")
            return

        pesan = QMessageBox.question(self, "Konfirmasi", "Yakin hapus data keluarga ini?", QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            self.crud.hapusKeluarga(self.id_terpilih)
            self.tampilData()
            self.doBersihKeluarga()
            QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")

    def doBersihKeluarga(self):
        """Reset form dan variabel ID"""
        self.id_terpilih = None
        self.formKeluarga.nAMAKEPALAKELUARGALineEdit.clear()
        self.formKeluarga.aLAMATLineEdit.clear()
        self.formKeluarga.jUMLAHANGGOTASpinBox.setValue(0)
        self.formKeluarga.sTATUSEKONOMIComboBox.setCurrentIndex(0)
        self.formKeluarga.iDUSAHAComboBox.setCurrentIndex(0)
        self.formKeluarga.dIBUATOLEHComboBox.setCurrentIndex(0)

    def tampilData(self):
        baris = self.crud.dataKeluarga()
        self.formKeluarga.tabelKeluarga.setRowCount(0)
        for r in baris:
            i = self.formKeluarga.tabelKeluarga.rowCount()
            self.formKeluarga.tabelKeluarga.insertRow(i)
            self.formKeluarga.tabelKeluarga.setItem(i, 0, QTableWidgetItem(str(r["id_keluarga"])))
            self.formKeluarga.tabelKeluarga.setItem(i, 1, QTableWidgetItem(r["nama_kepala_keluarga"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 2, QTableWidgetItem(r["alamat"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 3, QTableWidgetItem(str(r["jumlah_anggota"])))
            self.formKeluarga.tabelKeluarga.setItem(i, 4, QTableWidgetItem(r["status_ekonomi"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 5, QTableWidgetItem(str(r["id_usaha"])))

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
            self.formKeluarga.tabelKeluarga.setItem(i, 3, QTableWidgetItem(str(r["jumlah_anggota"])))
            self.formKeluarga.tabelKeluarga.setItem(i, 4, QTableWidgetItem(r["status_ekonomi"] or ""))
            self.formKeluarga.tabelKeluarga.setItem(i, 5, QTableWidgetItem(str(r["id_usaha"])))
