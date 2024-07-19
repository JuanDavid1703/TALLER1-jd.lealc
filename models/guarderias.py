from db import db
from models.perros import Perros
from models.cuidadores import Cuidadores

class Guarderias(db.Model):
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    nombre=db.Column(db.String(50), nullable=False)
    direccion=db.Column(db.String(50), nullable=False)
    telefono=db.Column(db.Integer, nullable=False)
    
    cuidadores = db.relationship('Cuidadores', backref="guarderias", lazy=True)
    perros = db.relationship('Perros', backref="guarderias", lazy=True)