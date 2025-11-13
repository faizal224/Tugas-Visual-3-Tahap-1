# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Pendaftaran(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("pendaftaran.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editNoDaftar.clear()
        self.ui.editIDAdmin.clear()
        self.ui.editKodeKel.clear()
        self.ui.editTglDaftar.clear()
        self.ui.editTglNikah.clear()
        self.ui.editStatus.clear()

    def simpan(self):
        if not self.ui.editNoDaftar.text():
            QMessageBox.warning(self, "Eror", "No Pendaftaran Kosong")
            return
        self.aksi.simpanDaftar(
            self.ui.editNoDaftar.text(), self.ui.editIDAdmin.text(), self.ui.editKodeKel.text(),
            self.ui.editTglDaftar.text(), self.ui.editTglNikah.text(), self.ui.editStatus.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahDaftar(
            self.ui.editNoDaftar.text(), self.ui.editIDAdmin.text(), self.ui.editKodeKel.text(),
            self.ui.editTglDaftar.text(), self.ui.editTglNikah.text(), self.ui.editStatus.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusDaftar(self.ui.editNoDaftar.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataDaftar()
        self.ui.tabelDaftar.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelDaftar.insertRow(i)
            self.ui.tabelDaftar.setItem(i, 0, QTableWidgetItem(str(row['no_pendaftaran'])))
            self.ui.tabelDaftar.setItem(i, 1, QTableWidgetItem(str(row['id_admin'])))
            self.ui.tabelDaftar.setItem(i, 2, QTableWidgetItem(str(row['tgl_pernikahan'])))
            self.ui.tabelDaftar.setItem(i, 3, QTableWidgetItem(str(row['status'])))
