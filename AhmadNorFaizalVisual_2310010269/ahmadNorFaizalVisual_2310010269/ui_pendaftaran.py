# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pendaftaran.ui'
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

class Ui_FormDaftar(object):
    def setupUi(self, FormDaftar):
        if not FormDaftar.objectName():
            FormDaftar.setObjectName(u"FormDaftar")
        FormDaftar.resize(700, 600)
        self.formLayoutWidget = QWidget(FormDaftar)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 200))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.l1 = QLabel(self.formLayoutWidget)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.editNoDaftar = QLineEdit(self.formLayoutWidget)
        self.editNoDaftar.setObjectName(u"editNoDaftar")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editNoDaftar)

        self.l2 = QLabel(self.formLayoutWidget)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.editIDAdmin = QLineEdit(self.formLayoutWidget)
        self.editIDAdmin.setObjectName(u"editIDAdmin")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIDAdmin)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editKodeKel = QLineEdit(self.formLayoutWidget)
        self.editKodeKel.setObjectName(u"editKodeKel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editKodeKel)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editTglDaftar = QLineEdit(self.formLayoutWidget)
        self.editTglDaftar.setObjectName(u"editTglDaftar")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTglDaftar)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editTglNikah = QLineEdit(self.formLayoutWidget)
        self.editTglNikah.setObjectName(u"editTglNikah")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTglNikah)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.editStatus = QLineEdit(self.formLayoutWidget)
        self.editStatus.setObjectName(u"editStatus")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editStatus)

        self.btnSimpan = QPushButton(FormDaftar)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 240, 90, 29))
        self.btnHapus = QPushButton(FormDaftar)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 240, 90, 29))
        self.btnUbah = QPushButton(FormDaftar)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 240, 90, 29))
        self.btnBersih = QPushButton(FormDaftar)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 240, 90, 29))
        self.tabelDaftar = QTableWidget(FormDaftar)
        if (self.tabelDaftar.columnCount() < 4):
            self.tabelDaftar.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelDaftar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelDaftar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelDaftar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelDaftar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelDaftar.setObjectName(u"tabelDaftar")
        self.tabelDaftar.setGeometry(QRect(50, 290, 600, 250))

        self.retranslateUi(FormDaftar)

        QMetaObject.connectSlotsByName(FormDaftar)
    # setupUi

    def retranslateUi(self, FormDaftar):
        FormDaftar.setWindowTitle(QCoreApplication.translate("FormDaftar", u"Form Pendaftaran", None))
        self.l1.setText(QCoreApplication.translate("FormDaftar", u"No Pendaftaran", None))
        self.l2.setText(QCoreApplication.translate("FormDaftar", u"ID Admin", None))
        self.l3.setText(QCoreApplication.translate("FormDaftar", u"Kode Kelurahan", None))
        self.l4.setText(QCoreApplication.translate("FormDaftar", u"Tgl Pendaftaran", None))
        self.l5.setText(QCoreApplication.translate("FormDaftar", u"Tgl Pernikahan", None))
        self.l6.setText(QCoreApplication.translate("FormDaftar", u"Status", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormDaftar", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormDaftar", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormDaftar", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormDaftar", u"Bersih", None))
        ___qtablewidgetitem = self.tabelDaftar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormDaftar", u"No Daftar", None));
        ___qtablewidgetitem1 = self.tabelDaftar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormDaftar", u"ID Admin", None));
        ___qtablewidgetitem2 = self.tabelDaftar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormDaftar", u"Tgl Nikah", None));
        ___qtablewidgetitem3 = self.tabelDaftar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormDaftar", u"Status", None));
    # retranslateUi

