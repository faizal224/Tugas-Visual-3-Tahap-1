# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class MempelaiWanita(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("wanita.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editIDUser.clear()
        self.ui.editNoDaftar.clear()
        self.ui.editNama.clear()
        self.ui.editTempat.clear()
        self.ui.editTgl.clear()
        self.ui.editUsia.clear()
        self.ui.editKWN.clear()
        self.ui.editAgama.clear()
        self.ui.editKerja.clear()
        self.ui.editAlamat.clear()
        self.ui.editPend.clear()
        self.ui.editStatus.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Mempelai Wajib Diisi")
            return
        self.aksi.simpanWanita(
            self.ui.editID.text(), self.ui.editIDUser.text(), self.ui.editNoDaftar.text(),
            self.ui.editNama.text(), self.ui.editTempat.text(), self.ui.editTgl.text(),
            self.ui.editUsia.text(), self.ui.editKWN.text(), self.ui.editAgama.text(),
            self.ui.editKerja.text(), self.ui.editAlamat.text(), self.ui.editPend.text(), self.ui.editStatus.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahWanita(
            self.ui.editID.text(), self.ui.editIDUser.text(), self.ui.editNoDaftar.text(),
            self.ui.editNama.text(), self.ui.editTempat.text(), self.ui.editTgl.text(),
            self.ui.editUsia.text(), self.ui.editKWN.text(), self.ui.editAgama.text(),
            self.ui.editKerja.text(), self.ui.editAlamat.text(), self.ui.editPend.text(), self.ui.editStatus.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusWanita(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataWanita()
        self.ui.tabelWanita.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelWanita.insertRow(i)
            self.ui.tabelWanita.setItem(i, 0, QTableWidgetItem(str(row['id_mempelai_perempuan'])))
            self.ui.tabelWanita.setItem(i, 1, QTableWidgetItem(str(row['nama'])))
            self.ui.tabelWanita.setItem(i, 2, QTableWidgetItem(str(row['no_pendaftaran'])))
            self.ui.tabelWanita.setItem(i, 3, QTableWidgetItem(str(row['alamat'])))
            self.ui.tabelWanita.setItem(i, 4, QTableWidgetItem(str(row['agama'])))
