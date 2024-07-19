from flask_login import UserMixin
from db import db

class Usuarios(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(45), nullable=False)
    contrasenia = db.Column(db.String(45), nullable=False)
    es_administrador = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, id, nombre_usuario, contrasenia, es_admin):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contrasenia = contrasenia
        self.es_administardor = es_admin