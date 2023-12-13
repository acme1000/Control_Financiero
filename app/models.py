from . import db
from datetime import date

class Movimiento(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tipo = db.Column(db.String(10))
    nombre=db.Column(db.String(20))
    monto=db.Column(db.Float(12))
    fecha=db.Column(db.Date)
    descr=db.Column(db.String(38))
    