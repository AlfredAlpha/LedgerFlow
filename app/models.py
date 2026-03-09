from . import db
from flask_login import UserMixin

class Colaborador(UserMixin, db.Model):
    __tablename__ = "colaboradores"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    cargo = db.Column(db.String(120), nullable=False)

class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    empresa = db.Column(db.String(120), nullable=False)
    cidade = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    telefone = db.Column(db.String(30))
    documento = db.Column(db.String(30))

class Mensalidade(db.Model):
    __tablename__ = "mensalidades"
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    vencimento = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pendente")
    codigo_boleto = db.Column(db.String(120))
    cliente = db.relationship("Cliente", backref="mensalidades")
