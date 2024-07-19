from db import db
from models.perros import Perros

class Cuidadores(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    nombre=db.Column(db.String(50), nullable=False)
    telefono=db.Column(db.Integer, nullable=False)
    id_Guarderia=db.Column(db.Integer,db.ForeignKey("guarderias.id"), nullable=False)
    perros = db.relationship('Perros', backref="cuidadores", lazy=True)