# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class DataPekerja(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Load UI File
        ui_file = QFile("DataPekerja.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formPekerja = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        # 2. Koneksi Tombol CRUD
        self.formPekerja.pushButton.clicked.connect(self.doSimpanPekerja)      # Simpan
        self.formPekerja.pushButton_4.clicked.connect(self.doUbahPekerja)     # Ubah
        self.formPekerja.pushButton_2.clicked.connect(self.doHapusPekerja)    # Hapus
        self.formPekerja.pushButton_3.clicked.connect(self.doBersihPekerja)   # Bersih

        # 3. Koneksi Tabel (Signal Klik) & Pencarian
        self.formPekerja.tableWidget.cellClicked.connect(self.getData)
        self.formPekerja.EditCari.textChanged.connect(self.doCariPekerja)

        # 4. Inisialisasi Data (ComboBox & Tabel)
        self.muatComboUsaha()
        self.muatComboKeluarga()
        self.muatComboAdmin()
        self.tampilData()

    def getData(self, row, col):
        """Mengambil data dari tabel dan menampilkannya kembali di form input"""
        # Mapping Kolom Tabel
        item_id        = self.formPekerja.tableWidget.item(row, 0) # id_pekerja
        item_nama      = self.formPekerja.tableWidget.item(row, 1) # nama_pekerja
        item_jk        = self.formPekerja.tableWidget.item(row, 2) # jenis_kelamin
        item_pekerjaan = self.formPekerja.tableWidget.item(row, 3) # pekerjaan
        item_gaji      = self.formPekerja.tableWidget.item(row, 4) # gaji
        item_id_usaha  = self.formPekerja.tableWidget.item(row, 5) # id_usaha
        item_id_kel    = self.formPekerja.tableWidget.item(row, 6) # id_keluarga
        item_admin     = self.formPekerja.tableWidget.item(row, 7) # dibuat_oleh (admin)

        # 1. Isi LineEdit (Nama, Pekerjaan, Gaji)
        # Jika Anda punya LineEdit untuk ID Pekerja, tambahkan di sini (misal: iDPEKERJALineEdit)
        if item_nama: self.formPekerja.nAMAPEKERJALineEdit.setText(item_nama.text())
        if item_pekerjaan: self.formPekerja.pEKERJAANLineEdit.setText(item_pekerjaan.text())
        if item_gaji: self.formPekerja.gajiLineEdit.setText(item_gaji.text())

        # 2. Isi ComboBox Jenis Kelamin (Teks Biasa)
        if item_jk:
            self.formPekerja.jENISKELAMINComboBox.setCurrentText(item_jk.text())

        # 3. Isi ComboBox Foreign Key (Mencari berdasarkan ID/Data)
        if item_id_usaha:
            idx = self.formPekerja.comboBox.findData(int(item_id_usaha.text()))
            self.formPekerja.comboBox.setCurrentIndex(idx)

        if item_id_kel:
            idx_kel = self.formPekerja.comboBox_2.findData(int(item_id_kel.text()))
            self.formPekerja.comboBox_2.setCurrentIndex(idx_kel)

        if item_admin:
            idx_adm = self.formPekerja.comboBox_3.findData(int(item_admin.text()))
            self.formPekerja.comboBox_3.setCurrentIndex(idx_adm)

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
            QMessageBox.information(self, "Informasi", "Nama Pekerja belum di isi")
            self.formPekerja.nAMAPEKERJALineEdit.setFocus()
        elif self.formPekerja.comboBox.currentData() is None:
            QMessageBox.information(self, "Informasi", "ID Usaha belum dipilih")
            self.formPekerja.comboBox.setFocus()
        else:
            pesan = QMessageBox.question(self, "Konfirmasi", "Simpan data pekerja ini?", QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                self.crud.simpanPekerja(
                    self.formPekerja.nAMAPEKERJALineEdit.text(),
                    self.formPekerja.jENISKELAMINComboBox.currentText(),
                    self.formPekerja.pEKERJAANLineEdit.text(),
                    self.formPekerja.gajiLineEdit.text(),
                    self.formPekerja.comboBox.currentData(),
                    self.formPekerja.comboBox_2.currentData(),
                    self.formPekerja.comboBox_3.currentData()
                )
                self.tampilData()
                self.doBersihPekerja()
                QMessageBox.information(self, "Informasi", "Data Berhasil Disimpan")

    def doUbahPekerja(self):
        # Catatan: Fungsi ubah biasanya membutuhkan ID Pekerja sebagai parameter di SQL
        self.crud.ubahPekerja(
            self.formPekerja.nAMAPEKERJALineEdit.text(),
            self.formPekerja.jENISKELAMINComboBox.currentText(),
            self.formPekerja.pEKERJAANLineEdit.text(),
            self.formPekerja.gajiLineEdit.text(),
            self.formPekerja.comboBox.currentData(),
            self.formPekerja.comboBox_2.currentData(),
            self.formPekerja.comboBox_3.currentData()
        )
        self.tampilData()
        QMessageBox.information(self, "Informasi", "Data berhasil diubah")

    def doHapusPekerja(self):
        tempIDUsaha    = self.formPekerja.comboBox.currentData()
        tempIDKeluarga = self.formPekerja.comboBox_2.currentData()

        if tempIDUsaha is None or tempIDKeluarga is None:
            QMessageBox.warning(self, "Peringatan", "Pilih data di tabel untuk dihapus")
            return

        pesan = QMessageBox.question(self, "Konfirmasi", "Yakin hapus data pekerja ini?", QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            self.crud.hapusPekerja(tempIDUsaha, tempIDKeluarga)
            self.tampilData()
            self.doBersihPekerja()
            QMessageBox.information(self, "Informasi", "Data berhasil dihapus")

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
            self.formPekerja.tableWidget.setItem(i, 0, QTableWidgetItem(str(r.get("id_pekerja", ""))))
            self.formPekerja.tableWidget.setItem(i, 1, QTableWidgetItem(r.get("nama_pekerja") or ""))
            self.formPekerja.tableWidget.setItem(i, 2, QTableWidgetItem(r.get("jenis_kelamin") or ""))
            self.formPekerja.tableWidget.setItem(i, 3, QTableWidgetItem(r.get("pekerjaan") or ""))

            gaji = r.get("gaji")
            gaji_text = "" if gaji is None else f"{float(gaji):.2f}"
            self.formPekerja.tableWidget.setItem(i, 4, QTableWidgetItem(gaji_text))

            self.formPekerja.tableWidget.setItem(i, 5, QTableWidgetItem(str(r.get("id_usaha", ""))))
            self.formPekerja.tableWidget.setItem(i, 6, QTableWidgetItem(str(r.get("id_keluarga", ""))))
            self.formPekerja.tableWidget.setItem(i, 7, QTableWidgetItem(str(r.get("dibuat_oleh", ""))))

    def doCariPekerja(self):
        cari = self.formPekerja.EditCari.text()
        baris = self.crud.CariPekerja(cari)
        self.formPekerja.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formPekerja.tableWidget.rowCount()
            self.formPekerja.tableWidget.insertRow(i)
            self.formPekerja.tableWidget.setItem(i, 0, QTableWidgetItem(str(r.get("id_pekerja", ""))))
            self.formPekerja.tableWidget.setItem(i, 1, QTableWidgetItem(r.get("nama_pekerja") or ""))
            self.formPekerja.tableWidget.setItem(i, 2, QTableWidgetItem(r.get("jenis_kelamin") or ""))
            self.formPekerja.tableWidget.setItem(i, 3, QTableWidgetItem(r.get("pekerjaan") or ""))

            gaji = r.get("gaji")
            gaji_text = "" if gaji is None else f"{float(gaji):.2f}"
            self.formPekerja.tableWidget.setItem(i, 4, QTableWidgetItem(gaji_text))

            self.formPekerja.tableWidget.setItem(i, 5, QTableWidgetItem(str(r.get("id_usaha", ""))))
            self.formPekerja.tableWidget.setItem(i, 6, QTableWidgetItem(str(r.get("id_keluarga", ""))))
            self.formPekerja.tableWidget.setItem(i, 7, QTableWidgetItem(str(r.get("dibuat_oleh", ""))))
