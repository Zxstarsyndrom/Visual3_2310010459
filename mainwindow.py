import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from DataAdmin import DataAdmin
from DataUsaha import DataUsaha
from DataKeluarga import DataKeluarga
from Kesejahteraan import Kesejahteraan
from DataPekerja import DataPekerja
from Pendampingan import Pendampingan
from Resiko import Resiko
from Baya import Baya



class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Variable untuk menampung file main.ui
        fileformutama = QFile("form.ui")

        # Membuka file UI hanya untuk dibaca
        if not fileformutama.open(QFile.ReadOnly):
            print("Gagal membuka file main.ui")
            return

        # Membuat objek loader untuk membaca file UI
        formloader = QUiLoader()

        # Load UI ke dalam objek formutama
        self.formutama = formloader.load(fileformutama, self)

        # Tutup file setelah selesai di-load (sangat disarankan)
        fileformutama.close()

        # Set layout utama dari file UI ke dalam QMainWindow
        self.setCentralWidget(self.formutama)

        # Jika main.ui punya menu bar
        if hasattr(self.formutama, 'menuBar'):
            self.setMenuBar(self.formutama.menuBar())

        # Sesuaikan ukuran window dengan desain UI
        self.resize(self.formutama.size())
        self.formutama.actionData_Admin.triggered.connect(self.bukaDataAdmin)
        self.formutama.actionData_Usaha.triggered.connect(self.bukaDataUsaha)
        self.formutama.actionData_Keluarga.triggered.connect(self.bukaDataKeluarga)
        self.formutama.actionData_Pekerja.triggered.connect(self.bukaDataPekerja)
        self.formutama.actionKesejahteraan.triggered.connect(self.bukaKesejahteraan)
        self.formutama.actionPendampingan.triggered.connect(self.bukaPendampingan)
        self.formutama.actionresiko.triggered.connect(self.bukaDataResiko)
        self.formutama.actionBAYA.triggered.connect(self.bukaBaya)

    def bukaBaya(self):
        """Fungsi untuk membuka Baya.ui"""
        self.window_Baya = Baya()
        self.window_Baya.show()
    def bukaDataAdmin(self):
        """Fungsi untuk membuka DataAdmin.ui"""
        self.window_admin = DataAdmin()
        self.window_admin.show()
    def bukaDataUsaha(self):
        """Fungsi membuka form DataUsaha.ui"""
        self.window_usaha = DataUsaha()
        self.window_usaha.show()
    def bukaDataKeluarga(self):
        """Fungsi membuka form DataKeluarga.ui"""
        self.window_keluarga = DataKeluarga()
        self.window_keluarga.show()
    def bukaDataPekerja(self):
        """Fungsi membuka form DataPekerja.ui"""
        self.window_pekerja = DataPekerja()
        self.window_pekerja.show()
    def bukaKesejahteraan(self):
        """Fungsi membuka form Kesejahteraan.ui"""
        self.window_kesejahteraan = Kesejahteraan()
        self.window_kesejahteraan.show()
    def bukaPendampingan (self):
        """Fungsi membuka form Pendampingan.ui"""
        self.window_Pendampingan = Pendampingan()
        self.window_Pendampingan.show()
    def bukaDataResiko(self):
        """Fungsi membuka form resiko.ui"""
        self.window_resiko = Resiko()
        self.window_resiko.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = main()
    widget.show()
    sys.exit(app.exec())
