# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class Resiko(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("Resiko.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formResiko = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()

        self.formResiko.pushButton.clicked.connect(self.doSimpanResiko)
        self.formResiko.pushButton_4.clicked.connect(self.doUbahResiko)
        self.formResiko.pushButton_2.clicked.connect(self.doHapusResiko)
        self.formResiko.pushButton_3.clicked.connect(self.doBersihResiko)

        self.muatComboPekerja()
        self.muatComboAdmin()
        self.setupTable()
        self.tampilData()
        self.formResiko.EditCari.textChanged.connect(self.doCariResiko)

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
            QMessageBox.information(None, "Informasi", "ID Pekerja belum dipilih")
            self.formResiko.comboBox_2.setFocus()
        elif not self.formResiko.jENISRESIKOLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Jenis Risiko belum di isi")
            self.formResiko.jENISRESIKOLineEdit.setFocus()
        elif not self.formResiko.comboBox.currentText().strip():
            QMessageBox.information(None, "Informasi", "Tingkat Risiko belum dipilih")
            self.formResiko.comboBox.setFocus()
        elif not self.formResiko.tINDAKANPENCEGAHANLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Tindakan Pencegahan belum di isi")
            self.formResiko.tINDAKANPENCEGAHANLineEdit.setFocus()
        elif not self.formResiko.tANGGALINSIDENDateEdit.date().isValid():
            QMessageBox.information(None, "Informasi", "Tanggal Insiden belum valid")
            self.formResiko.tANGGALINSIDENDateEdit.setFocus()
        elif self.formResiko.comboBox_3.currentData() is None:
            QMessageBox.information(None, "Informasi", "Dibuat Oleh belum dipilih")
            self.formResiko.comboBox_3.setFocus()
        else:
            pesan = QMessageBox.information(
                None,
                "Informasi",
                "Apakah Anda Yakin Menyimpan Data Ini?",
                QMessageBox.Yes | QMessageBox.No
            )
            if pesan == QMessageBox.Yes:
                tempIDPekerja   = self.formResiko.comboBox_2.currentData()
                tempJenisResiko = self.formResiko.jENISRESIKOLineEdit.text()
                tempTingkat     = self.formResiko.comboBox.currentText()
                tempTindakan    = self.formResiko.tINDAKANPENCEGAHANLineEdit.text()
                tempTanggal     = self.formResiko.tANGGALINSIDENDateEdit.date().toString("yyyy-MM-dd")
                tempDibuatOleh  = self.formResiko.comboBox_3.currentData()

                tingkat_enum = (tempTingkat or "").strip().lower()

                self.crud.simpanResiko(
                    tempIDPekerja,
                    tempJenisResiko,
                    tingkat_enum,
                    tempTindakan,
                    tempTanggal,
                    tempDibuatOleh
                )
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")
            else:
                pass

    def doUbahResiko(self):
        tempIDPekerja   = self.formResiko.comboBox_2.currentData()
        tempJenisResiko = self.formResiko.jENISRESIKOLineEdit.text()
        tempTingkat     = self.formResiko.comboBox.currentText()
        tempTindakan    = self.formResiko.tINDAKANPENCEGAHANLineEdit.text()
        tempTanggal     = self.formResiko.tANGGALINSIDENDateEdit.date().toString("yyyy-MM-dd")
        tempDibuatOleh  = self.formResiko.comboBox_3.currentData()

        tingkat_enum = (tempTingkat or "").strip().lower()

        self.crud.ubahResiko(
            tempIDPekerja,
            tempJenisResiko,
            tingkat_enum,
            tempTindakan,
            tempTanggal,
            tempDibuatOleh
        )
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def doHapusResiko(self):
        tempIDPekerja   = self.formResiko.comboBox_2.currentData()
        tempJenisResiko = self.formResiko.jENISRESIKOLineEdit.text()
        tempTanggal     = self.formResiko.tANGGALINSIDENDateEdit.date().toString("yyyy-MM-dd")
        self.crud.hapusResiko(tempIDPekerja, tempJenisResiko, tempTanggal)
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data berhasil dihapus")

    def doBersihResiko(self):
        self.formResiko.comboBox_2.setCurrentIndex(0)
        self.formResiko.jENISRESIKOLineEdit.clear()
        self.formResiko.comboBox.setCurrentIndex(1)
        self.formResiko.tINDAKANPENCEGAHANLineEdit.clear()
        self.formResiko.comboBox_3.setCurrentIndex(0)

    def tampilData(self):
        rows = self.crud.dataResiko()
        tbl = self.formResiko.tableWidget
        tbl.setRowCount(0)

        for r in rows:
            i = tbl.rowCount()
            tbl.insertRow(i)
            tbl.setItem(i, 0, QTableWidgetItem("" if r.get("id_pekerja") is None else str(r["id_pekerja"])))
            tbl.setItem(i, 1, QTableWidgetItem(r.get("jenis_risiko") or ""))
            tbl.setItem(i, 2, QTableWidgetItem(r.get("tingkat_risiko") or ""))
            tbl.setItem(i, 3, QTableWidgetItem(r.get("tindakan_pencegahan") or ""))
            tgl = r.get("tanggal_insiden")
            tbl.setItem(i, 4, QTableWidgetItem("" if tgl is None else str(tgl)))
            tbl.setItem(i, 5, QTableWidgetItem("" if r.get("dibuat_oleh") is None else str(r["dibuat_oleh"])))

    def doCariResiko(self):
        cari = self.formResiko.EditCari.text()
        baris = self.crud.CariResiko(cari)
        tbl = self.formResiko.tableWidget
        tbl.setRowCount(0)

        for r in baris:
            i = tbl.rowCount()
            tbl.insertRow(i)
            tbl.setItem(i, 0, QTableWidgetItem("" if r.get("id_pekerja") is None else str(r["id_pekerja"])))
            tbl.setItem(i, 1, QTableWidgetItem(r.get("jenis_risiko") or ""))
            tbl.setItem(i, 2, QTableWidgetItem(r.get("tingkat_risiko") or ""))
            tbl.setItem(i, 3, QTableWidgetItem(r.get("tindakan_pencegahan") or ""))
            tgl = r.get("tanggal_insiden")
            tbl.setItem(i, 4, QTableWidgetItem("" if tgl is None else str(tgl)))
            tbl.setItem(i, 5, QTableWidgetItem("" if r.get("dibuat_oleh") is None else str(r["dibuat_oleh"])))
