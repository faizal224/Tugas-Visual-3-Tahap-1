# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from pria import MempelaiPria
from wanita import MempelaiWanita
from pendaftaran import Pendaftaran
from validasi import Validasi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load(QFile("main.ui"), self)

        self.ui.actionPria.triggered.connect(self.buka_pria)
        self.ui.actionWanita.triggered.connect(self.buka_wanita)
        self.ui.actionDaftar.triggered.connect(self.buka_daftar)
        self.ui.actionValidasi.triggered.connect(self.buka_validasi)

    def buka_pria(self):
        self.window_pria = MempelaiPria()
        self.window_pria.show()

    def buka_wanita(self):
        self.window_wanita = MempelaiWanita()
        self.window_wanita.show()

    def buka_daftar(self):
        self.window_daftar = Pendaftaran()
        self.window_daftar.show()

    def buka_validasi(self):
        self.window_validasi = Validasi()
        self.window_validasi.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec())
