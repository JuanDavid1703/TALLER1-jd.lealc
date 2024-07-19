from db import db

class Perros(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    nombre=db.Column(db.String(50), nullable=False)
    raza=db.Column(db.String(50), nullable=False)
    edad=db.Column(db.Integer, nullable=False)
    peso=db.Column(db.Float, nullable=False)
    telefono=db.Column(db.Integer, nullable=False)
    id_Guarderia=db.Column(db.Integer,db.ForeignKey("guarderias.id"), nullable=False)
    id_Cuidador=db.Column(db.Integer,db.ForeignKey("cuidadores.id"), nullable=False)