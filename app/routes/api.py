from flask import Blueprint, jsonify
from ..models import Cliente

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/clientes")
def clientes():
    lista = Cliente.query.order_by(Cliente.id.asc()).all()
    data = []
    for c in lista:
        data.append({
            "id": c.id,
            "nome": c.nome,
            "empresa": c.empresa,
            "cidade": c.cidade,
            "email": c.email,
            "telefone": c.telefone,
            "documento": c.documento
        })
    return jsonify(data)
