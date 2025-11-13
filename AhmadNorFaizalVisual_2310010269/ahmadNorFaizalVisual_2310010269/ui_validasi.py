# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validasi.ui'
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

class Ui_FormValidasi(object):
    def setupUi(self, FormValidasi):
        if not FormValidasi.objectName():
            FormValidasi.setObjectName(u"FormValidasi")
        FormValidasi.resize(700, 600)
        self.formLayoutWidget = QWidget(FormValidasi)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 200))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.l1 = QLabel(self.formLayoutWidget)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.editNoVal = QLineEdit(self.formLayoutWidget)
        self.editNoVal.setObjectName(u"editNoVal")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editNoVal)

        self.l2 = QLabel(self.formLayoutWidget)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.editIDAdmin = QLineEdit(self.formLayoutWidget)
        self.editIDAdmin.setObjectName(u"editIDAdmin")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIDAdmin)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editNoDaftar = QLineEdit(self.formLayoutWidget)
        self.editNoDaftar.setObjectName(u"editNoDaftar")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editNoDaftar)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editTglVal = QLineEdit(self.formLayoutWidget)
        self.editTglVal.setObjectName(u"editTglVal")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTglVal)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editCatatan = QLineEdit(self.formLayoutWidget)
        self.editCatatan.setObjectName(u"editCatatan")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editCatatan)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.editHasil = QLineEdit(self.formLayoutWidget)
        self.editHasil.setObjectName(u"editHasil")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editHasil)

        self.btnSimpan = QPushButton(FormValidasi)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 240, 90, 29))
        self.btnHapus = QPushButton(FormValidasi)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 240, 90, 29))
        self.btnUbah = QPushButton(FormValidasi)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 240, 90, 29))
        self.btnBersih = QPushButton(FormValidasi)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 240, 90, 29))
        self.tabelValidasi = QTableWidget(FormValidasi)
        if (self.tabelValidasi.columnCount() < 4):
            self.tabelValidasi.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelValidasi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelValidasi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelValidasi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelValidasi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelValidasi.setObjectName(u"tabelValidasi")
        self.tabelValidasi.setGeometry(QRect(50, 290, 600, 250))

        self.retranslateUi(FormValidasi)

        QMetaObject.connectSlotsByName(FormValidasi)
    # setupUi

    def retranslateUi(self, FormValidasi):
        FormValidasi.setWindowTitle(QCoreApplication.translate("FormValidasi", u"Form Validasi", None))
        self.l1.setText(QCoreApplication.translate("FormValidasi", u"No Validasi", None))
        self.l2.setText(QCoreApplication.translate("FormValidasi", u"ID Admin", None))
        self.l3.setText(QCoreApplication.translate("FormValidasi", u"No Pendaftaran", None))
        self.l4.setText(QCoreApplication.translate("FormValidasi", u"Tgl Validasi", None))
        self.l5.setText(QCoreApplication.translate("FormValidasi", u"Catatan Tambahan", None))
        self.l6.setText(QCoreApplication.translate("FormValidasi", u"Hasil", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormValidasi", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormValidasi", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormValidasi", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormValidasi", u"Bersih", None))
        ___qtablewidgetitem = self.tabelValidasi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormValidasi", u"No Validasi", None));
        ___qtablewidgetitem1 = self.tabelValidasi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormValidasi", u"No Daftar", None));
        ___qtablewidgetitem2 = self.tabelValidasi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormValidasi", u"Tgl Val", None));
        ___qtablewidgetitem3 = self.tabelValidasi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormValidasi", u"Hasil", None));
    # retranslateUi

