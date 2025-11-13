# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pria.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_FormPria(object):
    def setupUi(self, FormPria):
        if not FormPria.objectName():
            FormPria.setObjectName(u"FormPria")
        FormPria.resize(800, 700)
        self.formLayoutWidget = QWidget(FormPria)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 700, 350))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.l1 = QLabel(self.formLayoutWidget)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.l2 = QLabel(self.formLayoutWidget)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.editIDUser = QLineEdit(self.formLayoutWidget)
        self.editIDUser.setObjectName(u"editIDUser")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIDUser)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editNoDaftar = QLineEdit(self.formLayoutWidget)
        self.editNoDaftar.setObjectName(u"editNoDaftar")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editNoDaftar)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editTempat = QLineEdit(self.formLayoutWidget)
        self.editTempat.setObjectName(u"editTempat")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTempat)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.editTgl = QLineEdit(self.formLayoutWidget)
        self.editTgl.setObjectName(u"editTgl")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editTgl)

        self.l7 = QLabel(self.formLayoutWidget)
        self.l7.setObjectName(u"l7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.l7)

        self.editUsia = QLineEdit(self.formLayoutWidget)
        self.editUsia.setObjectName(u"editUsia")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editUsia)

        self.l8 = QLabel(self.formLayoutWidget)
        self.l8.setObjectName(u"l8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.l8)

        self.editKWN = QLineEdit(self.formLayoutWidget)
        self.editKWN.setObjectName(u"editKWN")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.editKWN)

        self.l9 = QLabel(self.formLayoutWidget)
        self.l9.setObjectName(u"l9")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.l9)

        self.editAgama = QLineEdit(self.formLayoutWidget)
        self.editAgama.setObjectName(u"editAgama")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.editAgama)

        self.l10 = QLabel(self.formLayoutWidget)
        self.l10.setObjectName(u"l10")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.l10)

        self.editKerja = QLineEdit(self.formLayoutWidget)
        self.editKerja.setObjectName(u"editKerja")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.editKerja)

        self.l11 = QLabel(self.formLayoutWidget)
        self.l11.setObjectName(u"l11")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.l11)

        self.editAlamat = QLineEdit(self.formLayoutWidget)
        self.editAlamat.setObjectName(u"editAlamat")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.editAlamat)

        self.l12 = QLabel(self.formLayoutWidget)
        self.l12.setObjectName(u"l12")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.l12)

        self.editPend = QLineEdit(self.formLayoutWidget)
        self.editPend.setObjectName(u"editPend")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.editPend)

        self.l13 = QLabel(self.formLayoutWidget)
        self.l13.setObjectName(u"l13")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.l13)

        self.editStatus = QLineEdit(self.formLayoutWidget)
        self.editStatus.setObjectName(u"editStatus")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.editStatus)

        self.btnSimpan = QPushButton(FormPria)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 380, 90, 29))
        self.btnHapus = QPushButton(FormPria)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 380, 90, 29))
        self.btnUbah = QPushButton(FormPria)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 380, 90, 29))
        self.btnBersih = QPushButton(FormPria)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 380, 90, 29))
        self.tabelPria = QTableWidget(FormPria)
        if (self.tabelPria.columnCount() < 5):
            self.tabelPria.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPria.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPria.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPria.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPria.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelPria.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelPria.setObjectName(u"tabelPria")
        self.tabelPria.setGeometry(QRect(50, 430, 700, 250))

        self.retranslateUi(FormPria)

        QMetaObject.connectSlotsByName(FormPria)
    # setupUi

    def retranslateUi(self, FormPria):
        FormPria.setWindowTitle(QCoreApplication.translate("FormPria", u"Data Mempelai Laki-laki", None))
        self.l1.setText(QCoreApplication.translate("FormPria", u"ID Mempelai Laki", None))
        self.l2.setText(QCoreApplication.translate("FormPria", u"ID User", None))
        self.l3.setText(QCoreApplication.translate("FormPria", u"No Pendaftaran", None))
        self.l4.setText(QCoreApplication.translate("FormPria", u"Nama Lengkap", None))
        self.l5.setText(QCoreApplication.translate("FormPria", u"Tempat Lahir", None))
        self.l6.setText(QCoreApplication.translate("FormPria", u"Tanggal Lahir", None))
        self.l7.setText(QCoreApplication.translate("FormPria", u"Usia", None))
        self.l8.setText(QCoreApplication.translate("FormPria", u"Kewarganegaraan (KWN)", None))
        self.l9.setText(QCoreApplication.translate("FormPria", u"Agama", None))
        self.l10.setText(QCoreApplication.translate("FormPria", u"Pekerjaan", None))
        self.l11.setText(QCoreApplication.translate("FormPria", u"Alamat", None))
        self.l12.setText(QCoreApplication.translate("FormPria", u"Pendidikan", None))
        self.l13.setText(QCoreApplication.translate("FormPria", u"Status", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormPria", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormPria", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormPria", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormPria", u"Bersih", None))
        ___qtablewidgetitem = self.tabelPria.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormPria", u"ID", None));
        ___qtablewidgetitem1 = self.tabelPria.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormPria", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelPria.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormPria", u"No Daftar", None));
        ___qtablewidgetitem3 = self.tabelPria.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormPria", u"Alamat", None));
        ___qtablewidgetitem4 = self.tabelPria.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormPria", u"Agama", None));
    # retranslateUi

