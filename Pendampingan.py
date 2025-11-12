# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class Pendampingan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("Pendampingan.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formPendampingan = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.formPendampingan.pushButton.clicked.connect(self.doSimpanPendampingan)
        self.formPendampingan.pushButton_4.clicked.connect(self.doUbahPendampingan)
        self.formPendampingan.pushButton_2.clicked.connect(self.doHapusPendampingan)
        self.formPendampingan.pushButton_3.clicked.connect(self.doBersihPendampingan)

        self.muatComboUsaha()
        self.muatComboAdmin()

        self.tampilData()
        self.formPendampingan.EditCari.textChanged.connect(self.doCariPendampingan)

    def muatComboUsaha(self):
        cb = self.formPendampingan.comboBox
        cb.clear
        cb.addItem("— pilih usaha —", None)
        for r in self.crud.listUsaha():
            cb.addItem(f'{r["nama_usaha"]} (ID: {r["id_usaha"]})', r["id_usaha"])

    def muatComboAdmin(self):
        cb = self.formPendampingan.comboBox_2
        cb.clear()
        cb.addItem("— pilih admin —", None)
        for r in self.crud.listAdmin():
            cb.addItem(f'{r["username"]} (ID: {r["id_admin"]})', r["id_admin"])

    # ===== Tombol =====
    def doSimpanPendampingan(self):
        if not self.formPendampingan.nAMAPROGRAMLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Program belum di isi")
            self.formPendampingan.nAMAPROGRAMLineEdit.setFocus()
        elif not self.formPendampingan.tANGGALSELESAIDateEdit.date().toString("yyyy-MM-dd").strip():
            QMessageBox.information(None, "Informasi", "Tanggal Mulai belum di isi")
            self.formPendampingan.tANGGALSELESAIDateEdit.setFocus()
        elif not self.formPendampingan.tANGGALSELESAIDateEdit_2.date().toString("yyyy-MM-dd").strip():
            QMessageBox.information(None, "Informasi", "Tanggal Selesai belum di isi")
            self.formPendampingan.tANGGALSELESAIDateEdit_2.setFocus()
        elif not self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Lembaga Pendamping belum di isi")
            self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.setFocus()
        elif self.formPendampingan.comboBox.currentData() is None:
            QMessageBox.information(None, "Informasi", "ID Usaha belum dipilih")
            self.formPendampingan.comboBox.setFocus()
        elif self.formPendampingan.comboBox_2.currentData() is None:
            QMessageBox.information(None, "Informasi", "Dibuat Oleh belum dipilih")
            self.formPendampingan.comboBox_2.setFocus()
        else:
            pesan = QMessageBox.information(
                None,
                "Informasi",
                "Apakah Anda Yakin Menyimpan Data Ini?",
                QMessageBox.Yes | QMessageBox.No
            )
            if pesan == QMessageBox.Yes:
                nama_program       = self.formPendampingan.nAMAPROGRAMLineEdit.text()
                tanggal_mulai      = self.formPendampingan.tANGGALSELESAIDateEdit.date().toString("yyyy-MM-dd")
                tanggal_selesai    = self.formPendampingan.tANGGALSELESAIDateEdit_2.date().toString("yyyy-MM-dd")
                lembaga_pendamping = self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.text()
                id_usaha           = self.formPendampingan.comboBox.currentData()
                dibuat_oleh        = self.formPendampingan.comboBox_2.currentData()

                self.crud.simpanPendampingan(
                    nama_program, tanggal_mulai, tanggal_selesai,
                    lembaga_pendamping, id_usaha, dibuat_oleh
                )
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")
            else:
                pass

    def doUbahPendampingan(self):
        nama_program       = self.formPendampingan.nAMAPROGRAMLineEdit.text()
        tanggal_mulai      = self.formPendampingan.tANGGALSELESAIDateEdit.date().toString("yyyy-MM-dd")
        tanggal_selesai    = self.formPendampingan.tANGGALSELESAIDateEdit_2.date().toString("yyyy-MM-dd")
        lembaga_pendamping = self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.text()
        id_usaha           = self.formPendampingan.comboBox.currentData()
        dibuat_oleh        = self.formPendampingan.comboBox_2.currentData()

        self.crud.ubahPendampingan(
            nama_program, tanggal_mulai, tanggal_selesai,
            lembaga_pendamping, id_usaha, dibuat_oleh
        )
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def doHapusPendampingan(self):
        nama_program = self.formPendampingan.nAMAPROGRAMLineEdit.text()
        self.crud.hapusPendampingan(nama_program)
        QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    def doBersihPendampingan(self):
        self.formPendampingan.nAMAPROGRAMLineEdit.clear()
        self.formPendampingan.lEMBAGAPENDAMPINGLineEdit.clear()
        self.formPendampingan.comboBox.setCurrentIndex(0)
        self.formPendampingan.comboBox_2.setCurrentIndex(0)

    def tampilData(self):
        baris = self.crud.dataPendampingan()
        self.formPendampingan.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formPendampingan.tableWidget.rowCount()
            self.formPendampingan.tableWidget.insertRow(i)

            self.formPendampingan.tableWidget.setItem(i, 0, QTableWidgetItem("" if r.get("id_pendampingan") is None else str(r["id_pendampingan"])))
            self.formPendampingan.tableWidget.setItem(i, 1, QTableWidgetItem(r.get("nama_program") or ""))

            t_mulai   = r.get("tanggal_mulai")
            t_selesai = r.get("tanggal_selesai")
            self.formPendampingan.tableWidget.setItem(i, 2, QTableWidgetItem("" if t_mulai   is None else str(t_mulai)))
            self.formPendampingan.tableWidget.setItem(i, 3, QTableWidgetItem("" if t_selesai is None else str(t_selesai)))

            self.formPendampingan.tableWidget.setItem(i, 4, QTableWidgetItem(r.get("lembaga_pendamping") or ""))
            self.formPendampingan.tableWidget.setItem(i, 5, QTableWidgetItem("" if r.get("id_usaha")    is None else str(r["id_usaha"])))
            self.formPendampingan.tableWidget.setItem(i, 6, QTableWidgetItem("" if r.get("dibuat_oleh") is None else str(r["dibuat_oleh"])))

    def doCariPendampingan(self):
        cari = self.formPendampingan.EditCari.text()
        baris = self.crud.CariPendampingan(cari)
        self.formPendampingan.tableWidget.setRowCount(0)
        for r in baris:
            i = self.formPendampingan.tableWidget.rowCount()
            self.formPendampingan.tableWidget.insertRow(i)

            self.formPendampingan.tableWidget.setItem(i, 0, QTableWidgetItem("" if r.get("id_pendampingan") is None else str(r["id_pendampingan"])))
            self.formPendampingan.tableWidget.setItem(i, 1, QTableWidgetItem(r.get("nama_program") or ""))

            t_mulai   = r.get("tanggal_mulai")
            t_selesai = r.get("tanggal_selesai")
            self.formPendampingan.tableWidget.setItem(i, 2, QTableWidgetItem("" if t_mulai   is None else str(t_mulai)))
            self.formPendampingan.tableWidget.setItem(i, 3, QTableWidgetItem("" if t_selesai is None else str(t_selesai)))

            self.formPendampingan.tableWidget.setItem(i, 4, QTableWidgetItem(r.get("lembaga_pendamping") or ""))
            self.formPendampingan.tableWidget.setItem(i, 5, QTableWidgetItem("" if r.get("id_usaha")    is None else str(r["id_usaha"])))
            self.formPendampingan.tableWidget.setItem(i, 6, QTableWidgetItem("" if r.get("dibuat_oleh") is None else str(r["dibuat_oleh"])))
