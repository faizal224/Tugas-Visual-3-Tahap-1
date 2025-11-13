# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Validasi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("validasi.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editNoVal.clear()
        self.ui.editIDAdmin.clear()
        self.ui.editNoDaftar.clear()
        self.ui.editTglVal.clear()
        self.ui.editCatatan.clear()
        self.ui.editHasil.clear()

    def simpan(self):
        if not self.ui.editNoVal.text():
            QMessageBox.warning(self, "Eror", "No Validasi Kosong")
            return
        self.aksi.simpanValidasi(
            self.ui.editNoVal.text(), self.ui.editIDAdmin.text(), self.ui.editNoDaftar.text(),
            self.ui.editTglVal.text(), self.ui.editCatatan.text(), self.ui.editHasil.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahValidasi(
            self.ui.editNoVal.text(), self.ui.editIDAdmin.text(), self.ui.editNoDaftar.text(),
            self.ui.editTglVal.text(), self.ui.editCatatan.text(), self.ui.editHasil.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusValidasi(self.ui.editNoVal.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataValidasi()
        self.ui.tabelValidasi.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelValidasi.insertRow(i)
            self.ui.tabelValidasi.setItem(i, 0, QTableWidgetItem(str(row['no_validasi'])))
            self.ui.tabelValidasi.setItem(i, 1, QTableWidgetItem(str(row['no_pendaftaran'])))
            self.ui.tabelValidasi.setItem(i, 2, QTableWidgetItem(str(row['tgl_validasi'])))
            self.ui.tabelValidasi.setItem(i, 3, QTableWidgetItem(str(row['hasil'])))
