from sqlalchemy.orm import backref
from database import db

class Equipamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), unique=False, nullable=False)
    emprestimo = db.relationship('Emprestimo',backref='equipamento',lazy=True)