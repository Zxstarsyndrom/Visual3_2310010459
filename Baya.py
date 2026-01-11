from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb


class Baya(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file = QFile("Baya.ui")
        # setelah menampung main.ui dibuka dan tidak bisa di edit
        ui_file.open(QFile.ReadOnly)
        # membuat object loader ui
        loader = QUiLoader()
        self.formBaya = loader.load(ui_file, self)
        ui_file.close()

        self.crud = my_cruddb()
        self.formBaya.pushButton.clicked.connect(self.doSimpanBaya)
        self.formBaya.pushButton_2.clicked.connect(self.doUbahBaya)

        self.formBaya.hARGALineEdit.textChanged.connect(self.hitungTotal)
        self.formBaya.jUMLAHLineEdit.textChanged.connect(self.hitungTotal)
        self.formBaya.tablebaya.cellClicked.connect(self.getData)
        self.formBaya.tOTALLineEdit.setReadOnly(True)

        self.tampilData()

    def hitungTotal(self):
            try:
                # 1. Ambil nilai input
                harga_str = self.formBaya.hARGALineEdit.text() or "0"
                jumlah_str = self.formBaya.jUMLAHLineEdit.text() or "0"

                # 2. Konversi ke angka
                harga = float(harga_str)
                jumlah = float(jumlah_str)

                # 3. Hitung Subtotal (Harga x Jumlah)
                subtotal = harga * jumlah

                # 4. Hitung Nilai Diskon (0.7%)
                # Rumus: subtotal * 0.007
                nilai_diskon = subtotal * (0.7 / 100)

                # 5. Hitung Total Akhir setelah dipotong diskon
                total_akhir = subtotal - nilai_diskon

                # 6. Tampilkan ke tOTALLineEdit
                # Menggunakan round(total_akhir, 2) agar hanya ada 2 angka di belakang koma
                self.formBaya.tOTALLineEdit.setText(str(round(total_akhir, 2)))

            except ValueError:
                self.formBaya.tOTALLineEdit.setText("0")

    def doSimpanBaya(self):
        if not self.formBaya.kodeLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "KODE belum di isi")
            self.formBaya.kodeLineEdit.setFocus()
        elif not self.formBaya.nAMABARANGLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "NAMA_BARANG belum di isi")
            self.formBaya.nAMABARANGLineEdit.setFocus()
        elif not self.formBaya.hARGALineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "HARGA belum di isi")
            self.formBaya.hARGALineEdit.setFocus()
        elif not self.formBaya.jUMLAHLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "JUMLAH belum di isi")
            self.formBaya.jUMLAHLineEdit.setFocus()
        else:
            pesan = QMessageBox.information(
                None,
                "Informasi",
                "Apakah Anda Yakin Menyimpan Data Ini?",
                QMessageBox.Yes | QMessageBox.No
            )
            if pesan == QMessageBox.Yes:
                tempkode = self.formBaya.kodeLineEdit.text()
                tempnamabarang = self.formBaya.nAMABARANGLineEdit.text()
                tempharga     = self.formBaya.hARGALineEdit.text()
                tempjumlah    = self.formBaya.jUMLAHLineEdit.text()
                temptotal     = self.formBaya.tOTALLineEdit.text()
                self.crud.simpanBaya(tempkode, tempnamabarang, tempharga, tempjumlah, temptotal)
                self.tampilData()
                QMessageBox.information(None, "Informasi", "Data Berhasil di Simpan")
            else:
                pass

    def doUbahBaya(self):
        tempkode = self.formBaya.kodeLineEdit.text()
        tempnamabarang = self.formBaya.nAMABARANGLineEdit.text()
        tempharga     = self.formBaya.hARGALineEdit.text()
        tempjumlah    = self.formBaya.jUMLAHLineEdit.text()
        temptotal     = self.formBaya.tOTALLineEdit.text()
        self.crud.ubahBaya(tempkode, tempnamabarang, tempharga, tempjumlah, temptotal)
        self.tampilData()
        QMessageBox.information(None, "Informasi", "Data berhasil diubah")

    def tampilData(self):
        baris = self.crud.dataBaya()
        print(baris)
        self.formBaya.tablebaya.setRowCount(0)
        for r in baris:
            i = self.formBaya.tablebaya.rowCount()
            self.formBaya.tablebaya.insertRow(i)
            self.formBaya.tablebaya.setItem(i, 0, QTableWidgetItem(str(r["KODE"])))
            self.formBaya.tablebaya.setItem(i, 1, QTableWidgetItem(r["NAMA_BARANG"] or ""))
            self.formBaya.tablebaya.setItem(i, 2, QTableWidgetItem(str(r["HARGA"]) if r["HARGA"] else ""))
            self.formBaya.tablebaya.setItem(i, 3, QTableWidgetItem(str(r["JUMLAH"]) if r["JUMLAH"] else ""))
            self.formBaya.tablebaya.setItem(i, 4, QTableWidgetItem(str(r["TOTAL"]) if r["TOTAL"] else ""))

    def getData(self, row, col):
            # Mengambil data dari setiap kolom di baris yang diklik
            item_kode   = self.formBaya.tablebaya.item(row, 0)
            item_nama   = self.formBaya.tablebaya.item(row, 1)
            item_harga  = self.formBaya.tablebaya.item(row, 2)
            item_jumlah = self.formBaya.tablebaya.item(row, 3)
            item_total  = self.formBaya.tablebaya.item(row, 4)

            # Pastikan item tidak kosong sebelum mengambil teksnya
            if item_kode and item_nama and item_harga and item_jumlah and item_total:
                self.formBaya.kodeLineEdit.setText(item_kode.text())
                self.formBaya.nAMABARANGLineEdit.setText(item_nama.text())
                self.formBaya.hARGALineEdit.setText(item_harga.text())
                self.formBaya.jUMLAHLineEdit.setText(item_jumlah.text())
                self.formBaya.tOTALLineEdit.setText(item_total.text())

