from datetime import datetime
from sim import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(mahasiswa_id):
    return Tmahasiswa.query.get(int(mahasiswa_id))

class Tmahasiswa(db.Model,UserMixin): #tambahkan
    id = db.Column(db.Integer, primary_key=True)
    npm = db.Column(db.String(15), unique=True, nullable=False)
    nama = db.Column(db.String(20) , nullable=False)
    email = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    kelas = db.Column(db.String(20), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(20), nullable=False, default='default.jpg')
    pengaduans = db.relationship('Tpengaduan', backref='mahasiswa')#backref itu relasi/hubungan antar ttabel

    def __repr__(self):
        return f"Tmahasiswa('{self.npm}', '{self.nama}', '{self.email}', '{self.password}', '{self.kelas}', '{self.alamat}','{self.foto}')"

class Tpengaduan(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    subjek =db.Column(db.String(100), nullable=False)
    kategori =db.Column(db.String(100), nullable=False)
    detail_pengaduan =db.Column(db.String(100), nullable=False)
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mahasiswa_id = db.Column (db.Integer, db.ForeignKey('tmahasiswa.id'), nullable=False)

    def __repr__(self):
        return f"Tpengaduan('{self.subjek}', '{self.kategori}', {self.detail_pengaduan}', '{self.tgl_post}')"
