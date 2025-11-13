# This Python file uses the following encoding: utf-8
import mysql.connector

class crud:
    def __init__(self):
        self.koneksiDB = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_agama'
        )

    def simpanPria(self, id_mempelai, id_user, no_daftar, nama, tempat, tgl, usia, kwn, agama, kerja, alamat, pend, status):
        kursor = self.koneksiDB.cursor()
        sql = """INSERT INTO mempelai_laki_laki
                 (id_mempelai_laki, id_user, no_pendaftaran, nama, tempat_lahir, tgl_lahir, usia, kwn, agama, pekerjaan, alamat, pendidikan, status)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        val = (id_mempelai, id_user, no_daftar, nama, tempat, tgl, usia, kwn, agama, kerja, alamat, pend, status)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahPria(self, id_mempelai, id_user, no_daftar, nama, tempat, tgl, usia, kwn, agama, kerja, alamat, pend, status):
        kursor = self.koneksiDB.cursor()
        sql = """UPDATE mempelai_laki_laki SET
                 id_user=%s, no_pendaftaran=%s, nama=%s, tempat_lahir=%s, tgl_lahir=%s, usia=%s, kwn=%s, agama=%s, pekerjaan=%s, alamat=%s, pendidikan=%s, status=%s
                 WHERE id_mempelai_laki=%s"""
        val = (id_user, no_daftar, nama, tempat, tgl, usia, kwn, agama, kerja, alamat, pend, status, id_mempelai)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusPria(self, id_mempelai):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM mempelai_laki_laki WHERE id_mempelai_laki=%s", (id_mempelai,))
        self.koneksiDB.commit()
        kursor.close()

    def dataPria(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM mempelai_laki_laki ORDER BY id_mempelai_laki ASC")
        return kursor.fetchall()

    def simpanWanita(self, id_mempelai, id_user, no_daftar, nama, tempat, tgl, usia, kwn, agama, kerja, alamat, pend, status):
        kursor = self.koneksiDB.cursor()
        sql = """INSERT INTO mempelai_perempuan
                 (id_mempelai_perempuan, id_user, no_pendaftaran, nama, tempat_lahir, tgl_lahir, usia, kwn, agama, pekerjaan, alamat, pendidikan, status)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        val = (id_mempelai, id_user, no_daftar, nama, tempat, tgl, usia, kwn, agama, kerja, alamat, pend, status)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahWanita(self, id_mempelai, id_user, no_daftar, nama, tempat, tgl, usia, kwn, agama, kerja, alamat, pend, status):
        kursor = self.koneksiDB.cursor()
        sql = """UPDATE mempelai_perempuan SET
                 id_user=%s, no_pendaftaran=%s, nama=%s, tempat_lahir=%s, tgl_lahir=%s, usia=%s, kwn=%s, agama=%s, pekerjaan=%s, alamat=%s, pendidikan=%s, status=%s
                 WHERE id_mempelai_perempuan=%s"""
        val = (id_user, no_daftar, nama, tempat, tgl, usia, kwn, agama, kerja, alamat, pend, status, id_mempelai)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusWanita(self, id_mempelai):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM mempelai_perempuan WHERE id_mempelai_perempuan=%s", (id_mempelai,))
        self.koneksiDB.commit()
        kursor.close()

    def dataWanita(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM mempelai_perempuan ORDER BY id_mempelai_perempuan ASC")
        return kursor.fetchall()

    def simpanDaftar(self, no_daftar, id_admin, kode_kel, tgl_daftar, tgl_nikah, status):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO pendaftaran (no_pendaftaran, id_admin, kode_kelurahan, tgl_pendaftaran, tgl_pernikahan, status) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (no_daftar, id_admin, kode_kel, tgl_daftar, tgl_nikah, status)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahDaftar(self, no_daftar, id_admin, kode_kel, tgl_daftar, tgl_nikah, status):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE pendaftaran SET id_admin=%s, kode_kelurahan=%s, tgl_pendaftaran=%s, tgl_pernikahan=%s, status=%s WHERE no_pendaftaran=%s"
        val = (id_admin, kode_kel, tgl_daftar, tgl_nikah, status, no_daftar)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusDaftar(self, no_daftar):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM pendaftaran WHERE no_pendaftaran=%s", (no_daftar,))
        self.koneksiDB.commit()
        kursor.close()

    def dataDaftar(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM pendaftaran ORDER BY no_pendaftaran ASC")
        return kursor.fetchall()

    def simpanValidasi(self, no_val, id_admin, no_daftar, tgl_val, catatan, hasil):
        kursor = self.koneksiDB.cursor()
        sql = "INSERT INTO validasi (no_validasi, id_admin, no_pendaftaran, tgl_validasi, catatan_tambahan, hasil) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (no_val, id_admin, no_daftar, tgl_val, catatan, hasil)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def ubahValidasi(self, no_val, id_admin, no_daftar, tgl_val, catatan, hasil):
        kursor = self.koneksiDB.cursor()
        sql = "UPDATE validasi SET id_admin=%s, no_pendaftaran=%s, tgl_validasi=%s, catatan_tambahan=%s, hasil=%s WHERE no_validasi=%s"
        val = (id_admin, no_daftar, tgl_val, catatan, hasil, no_val)
        kursor.execute(sql, val)
        self.koneksiDB.commit()
        kursor.close()

    def hapusValidasi(self, no_val):
        kursor = self.koneksiDB.cursor()
        kursor.execute("DELETE FROM validasi WHERE no_validasi=%s", (no_val,))
        self.koneksiDB.commit()
        kursor.close()

    def dataValidasi(self):
        kursor = self.koneksiDB.cursor(dictionary=True)
        kursor.execute("SELECT * FROM validasi ORDER BY no_validasi ASC")
        return kursor.fetchall()
