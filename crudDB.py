# This Python file uses the following encoding: utf-8
import mysql.connector

class my_cruddb:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='visual3_2310010459'
        )

    # ===== referensi combobox =====
    def listUsaha(self):
        c = self.conn.cursor(dictionary=True)
        c.execute("SELECT id_usaha, nama_usaha FROM usaha_batu_kapur ORDER BY nama_usaha ASC")
        rows = c.fetchall()
        c.close()
        return rows

    def listKeluarga(self):
        c = self.conn.cursor(dictionary=True)
        c.execute("SELECT id_keluarga, nama_kepala_keluarga FROM keluarga ORDER BY id_keluarga ASC")
        rows = c.fetchall()
        c.close()
        return rows

    def listAdmin(self):
        c = self.conn.cursor(dictionary=True)
        c.execute("SELECT id_admin, username FROM admin ORDER BY username ASC")
        rows = c.fetchall()
        c.close()
        return rows
    def listPekerja(self):
        c = self.conn.cursor(dictionary=True)
        c.execute("SELECT id_pekerja, nama_pekerja FROM pekerja ORDER BY nama_pekerja ASC")
        rows = c.fetchall()
        c.close()
        return rows


    # =====================
    # ADMIN
    # =====================

    def simpanAdmin(self, username, password, nama_lengkap, email, role):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO admin
            (username, password, nama_lengkap, email, role)
            VALUES (%s, %s, %s, %s, %s)
        """
        val = (username, password, nama_lengkap, email, role)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def ubahAdmin(self, id_admin, username, password, nama_lengkap, email, role):
        cursor = self.conn.cursor()
        sql = """
            UPDATE admin
            SET username = %s,
                password = %s,
                nama_lengkap = %s,
                email = %s,
                role = %s
            WHERE id_admin = %s
        """
        val = (username, password, nama_lengkap, email, role, id_admin)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def hapusAdmin(self, id_admin):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM admin WHERE id_admin=%s", (id_admin,))
        self.conn.commit()
        affected = alamat.rowcount
        alamat.close()
        return affected

    def dataAdmin(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM admin ORDER BY id_admin ASC")
        record = cur.fetchall()
        cur.close()
        return record
    def CariAdmin(self, param):
        sql = "select * from admin where id_admin like %s or username like %s or nama_lengkap like %s or email like %s or role like %s"
        alamat = self.conn.cursor(dictionary=True)
        alamat.execute(sql, [f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    # =====================
    # USAHA
    # =====================

    def simpanUsaha(self, nama_usaha, lokasi, tahun_berdiri, jumlah_buruh, pendapatan_bulanan):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO usaha_batu_kapur
            (nama_usaha, lokasi, tahun_berdiri, jumlah_buruh, pendapatan_bulanan)
            VALUES (%s, %s, %s, %s, %s)
        """
        val = (nama_usaha, lokasi, tahun_berdiri, jumlah_buruh, pendapatan_bulanan)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def ubahUsaha(self, id_usaha, nama_usaha, lokasi, tahun_berdiri, jumlah_buruh, pendapatan_bulanan):
        cursor = self.conn.cursor()
        sql = """
            UPDATE usaha_batu_kapur
            SET nama_usaha=%s,
                lokasi=%s,
                tahun_berdiri=%s,
                jumlah_buruh=%s,
                pendapatan_bulanan=%s
            WHERE id_usaha=%s
        """
        val = (nama_usaha, lokasi, tahun_berdiri, jumlah_buruh, pendapatan_bulanan, id_usaha)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def hapusUsaha(self, id_usaha):
        cursor = self.conn.cursor()
        sql = "DELETE FROM usaha_batu_kapur WHERE id_usaha=%s"
        val = (id_usaha,)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def dataUsaha(self):
        alamat = self.conn.cursor(dictionary=True)
        alamat.execute("SELECT * FROM usaha_batu_kapur order by id_usaha asc")
        record = alamat.fetchall()
        alamat.close()
        return record
    def CariUsaha(self, param):
        sql = "select * from usaha_batu_kapur where id_usaha like %s or nama_usaha like %s or lokasi like %s or tahun_berdiri like %s or jumlah_buruh like %s or pendapatan_bulanan like %s"
        alamat = self.conn.cursor(dictionary=True)
        alamat.execute(sql, [f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    # =====================
    # KELUARGA
    # =====================

    def dataKeluarga(self):
        c = self.conn.cursor(dictionary=True)
        c.execute("select * from keluarga order by id_keluarga asc")
        rows = c.fetchall()
        c.close()
        return rows

    def simpanKeluarga(self, nama_kk, alamat, jml, status, id_usaha, dibuat_oleh):
        c = self.conn.cursor()
        c.execute("""
            insert into keluarga (nama_kepala_keluarga, alamat, jumlah_anggota, status_ekonomi, id_usaha, dibuat_oleh)
            values (%s,%s,%s,%s,%s,%s)
        """, (nama_kk, alamat, jml, status, id_usaha, dibuat_oleh))
        self.conn.commit()
        c.close()

    def ubahKeluarga(self, id_keluarga, nama_kk, alamat, jml, status, id_usaha, dibuat_oleh):
        c = self.conn.cursor()
        c.execute("""
            update keluarga
               set nama_kepala_keluarga=%s, alamat=%s, jumlah_anggota=%s, status_ekonomi=%s, id_usaha=%s, dibuat_oleh=%s
             where id_keluarga=%s
        """, (nama_kk, alamat, jml, status, id_usaha, dibuat_oleh, id_keluarga))
        self.conn.commit()
        c.close()

    def hapusKeluarga(self, id_keluarga):
        c = self.conn.cursor()
        c.execute("delete from keluarga where id_keluarga=%s", (id_keluarga,))
        self.conn.commit()
        c.close()
    def CariKeluarga(self, param):
        sql = ("select * from keluarga "
               "where id_keluarga like %s or nama_kepala_keluarga like %s or alamat like %s "
               "or jumlah_anggota like %s or status_ekonomi like %s or id_usaha like %s or dibuat_oleh like %s")
        alamat = self.conn.cursor(dictionary=True)
        alamat.execute(sql, [f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record



    # =====================
    # PEKERJA
    # =====================

    def dataPekerja(self):
        c = self.conn.cursor(dictionary=True)
        c.execute("SELECT * FROM pekerja ORDER BY id_pekerja ASC")
        rows = c.fetchall()
        c.close()
        return rows

    def simpanPekerja(self, nama_pekerja, jenis_kelamin, pekerjaan, gaji, id_usaha, id_keluarga, dibuat_oleh):
        c = self.conn.cursor()
        c.execute("""
            INSERT INTO pekerja
                (nama_pekerja, jenis_kelamin, pekerjaan, gaji, id_usaha, id_keluarga, dibuat_oleh)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (nama_pekerja, jenis_kelamin, pekerjaan, gaji, id_usaha, id_keluarga, dibuat_oleh))
        self.conn.commit()
        c.close()

    def ubahPekerja(self, id_pekerja, nama_pekerja, jenis_kelamin, pekerjaan, gaji, id_usaha, id_keluarga, dibuat_oleh):
        c = self.conn.cursor()
        c.execute("""
            UPDATE pekerja
               SET nama_pekerja=%s,
                   jenis_kelamin=%s,
                   pekerjaan=%s,
                   gaji=%s,
                   id_usaha=%s,
                   id_keluarga=%s,
                   dibuat_oleh=%s
             WHERE id_pekerja=%s
        """, (nama_pekerja, jenis_kelamin, pekerjaan, gaji, id_usaha, id_keluarga, dibuat_oleh, id_pekerja))
        self.conn.commit()
        c.close()

    def hapusPekerja(self, id_usaha, id_keluarga):
        c = self.conn.cursor()
        c.execute("DELETE FROM pekerja WHERE id_usaha=%s AND id_keluarga=%s", (id_usaha, id_keluarga))
        self.conn.commit()
        c.close()

    def CariPekerja(self, param):
        sql = ("select * from pekerja "
               "where id_pekerja like %s or nama_pekerja like %s or jenis_kelamin like %s "
               "or pekerjaan like %s or gaji like %s or id_usaha like %s or id_keluarga like %s or dibuat_oleh like %s")
        alamat = self.conn.cursor(dictionary=True)
        alamat.execute(sql, [f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    # =====================
    # KESEJAHTERAAN
    # =====================

    def dataKesejahteraan(self):
        c = self.conn.cursor(dictionary=True)
        c.execute("SELECT * FROM kesejahteraan ORDER BY id_kesejahteraan ASC")
        rows = c.fetchall()
        c.close()
        return rows

    def simpanKesejahteraan(self, id_keluarga, tahun, penghasilan, pendidikan_anak, status_rumah, kategori_ipm, dibuat_oleh):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO kesejahteraan
            (id_keluarga, tahun, penghasilan, pendidikan_anak, status_rumah, kategori_ipm, dibuat_oleh)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        val = (id_keluarga, tahun, penghasilan, pendidikan_anak, status_rumah, kategori_ipm, dibuat_oleh)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def ubahKesejahteraan(self, id_keluarga, tahun, penghasilan, pendidikan_anak, status_rumah, kategori_ipm, dibuat_oleh):
        cursor = self.conn.cursor()
        sql = """
            UPDATE kesejahteraan
               SET penghasilan=%s,
                   pendidikan_anak=%s,
                   status_rumah=%s,
                   kategori_ipm=%s,
                   dibuat_oleh=%s
             WHERE id_keluarga=%s AND tahun=%s
        """
        val = (penghasilan, pendidikan_anak, status_rumah, kategori_ipm, dibuat_oleh, id_keluarga, tahun)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def hapusKesejahteraan(self, id_keluarga, tahun):
        cursor = self.conn.cursor()
        sql = "DELETE FROM kesejahteraan WHERE id_keluarga=%s AND tahun=%s"
        cursor.execute(sql, (id_keluarga, tahun))
        self.conn.commit()
        cursor.close()

    def CariKesejahteraan(self, param):
        sql = ("SELECT * FROM kesejahteraan "
               "WHERE id_kesejahteraan LIKE %s OR id_keluarga LIKE %s OR tahun LIKE %s "
               "OR penghasilan LIKE %s OR pendidikan_anak LIKE %s OR status_rumah LIKE %s "
               "OR kategori_ipm LIKE %s OR dibuat_oleh LIKE %s")
        alamat = self.conn.cursor(dictionary=True)
        alamat.execute(sql, [f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    # =====================
    # PENDAMPINGAN
    # =====================

    def dataPendampingan(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("""
            SELECT
              id_pendampingan,
              nama_program,
              DATE_FORMAT(tanggal_mulai,  '%Y-%m-%d') AS tanggal_mulai,
              DATE_FORMAT(tanggal_selesai,'%Y-%m-%d') AS tanggal_selesai,
              lembaga_pendamping,
              id_usaha,
              dibuat_oleh
            FROM pendampingan
            ORDER BY id_pendampingan ASC
        """)
        rows = cur.fetchall()
        cur.close()
        return rows

    def simpanPendampingan(self, nama_program, tanggal_mulai, tanggal_selesai, lembaga_pendamping, id_usaha, dibuat_oleh):
        c = self.conn.cursor()
        c.execute("""
            INSERT INTO pendampingan
                (nama_program, tanggal_mulai, tanggal_selesai, lembaga_pendamping, id_usaha, dibuat_oleh)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (nama_program, tanggal_mulai, tanggal_selesai, lembaga_pendamping, id_usaha, dibuat_oleh))
        self.conn.commit()
        c.close()

    def ubahPendampingan(self, nama_program, tanggal_mulai, tanggal_selesai, lembaga_pendamping, id_usaha, dibuat_oleh):
        c = self.conn.cursor()
        c.execute("""
            UPDATE pendampingan
               SET tanggal_mulai=%s,
                   tanggal_selesai=%s,
                   lembaga_pendamping=%s,
                   id_usaha=%s,
                   dibuat_oleh=%s
             WHERE nama_program=%s
        """, (tanggal_mulai, tanggal_selesai, lembaga_pendamping, id_usaha, dibuat_oleh, nama_program))
        self.conn.commit()
        c.close()

    def hapusPendampingan(self, nama_program):
        c = self.conn.cursor()
        c.execute("DELETE FROM pendampingan WHERE nama_program=%s", (nama_program,))
        self.conn.commit()
        c.close()

    def CariPendampingan(self, param):
        sql = ("SELECT * FROM pendampingan "
               "WHERE id_pendampingan LIKE %s OR nama_program LIKE %s OR tanggal_mulai LIKE %s "
               "OR tanggal_selesai LIKE %s OR lembaga_pendamping LIKE %s OR id_usaha LIKE %s OR dibuat_oleh LIKE %s")
        alamat = self.conn.cursor(dictionary=True)
        alamat.execute(sql, [f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"])
        record = alamat.fetchall()
        alamat.close()
        return record

    # =====================
    # RESIKO / RISIKO_PEKERJAAN
    # =====================

    def simpanResiko(self, id_pekerja, jenis_risiko, tingkat_risiko, tindakan_pencegahan, tanggal_insiden, dibuat_oleh):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO risiko_pekerjaan
            (id_pekerja, jenis_risiko, tingkat_risiko, tindakan_pencegahan, tanggal_insiden, dibuat_oleh)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        val = (id_pekerja, jenis_risiko, tingkat_risiko, tindakan_pencegahan, tanggal_insiden, dibuat_oleh)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def ubahResiko(self, id_risiko, id_pekerja, jenis_risiko, tingkat_risiko, tindakan_pencegahan, tanggal_insiden, dibuat_oleh):
        cursor = self.conn.cursor()
        sql = """
            UPDATE risiko_pekerjaan
               SET id_pekerja=%s,
                   jenis_risiko=%s,
                   tingkat_risiko=%s,
                   tindakan_pencegahan=%s,
                   tanggal_insiden=%s,
                   dibuat_oleh=%s
             WHERE id_risiko=%s
        """
        val = (id_pekerja, jenis_risiko, tingkat_risiko, tindakan_pencegahan, tanggal_insiden, dibuat_oleh, id_risiko)
        cursor.execute(sql, val)
        self.conn.commit()
        cursor.close()

    def hapusResiko(self, id_risiko):
        alamat = self.conn.cursor()
        alamat.execute("DELETE FROM risiko_pekerjaan WHERE id_risiko=%s", (id_risiko,))
        self.conn.commit()
        affected = alamat.rowcount
        alamat.close()
        return affected

    def dataResiko(self):
        cur = self.conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM risiko_pekerjaan ORDER BY id_risiko ASC")
        record = cur.fetchall()
        cur.close()
        return record

    def CariResiko(self, param):
        sql = ("SELECT * FROM risiko_pekerjaan "
               "WHERE id_risiko LIKE %s OR id_pekerja LIKE %s OR jenis_risiko LIKE %s OR tingkat_risiko LIKE %s "
               "OR tindakan_pencegahan LIKE %s OR tanggal_insiden LIKE %s OR dibuat_oleh LIKE %s")
        alamat = self.conn.cursor(dictionary=True)
        like = f"%{param}%"
        alamat.execute(sql, [like, like, like, like, like, like, like])
        record = alamat.fetchall()
        alamat.close()
        return record
