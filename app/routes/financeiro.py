from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from ..models import Mensalidade, Cliente
from .. import db

bp = Blueprint("financeiro", __name__, url_prefix="/financeiro")

@bp.route("/mensalidades")
@login_required
def mensalidades():
    data = Mensalidade.query.order_by(Mensalidade.id.desc()).all()
    return render_template("mensalidades.html", data=data)

@bp.route("/boletos/novo", methods=["GET", "POST"])
@login_required
def novo_boleto():
    clientes = Cliente.query.order_by(Cliente.nome.asc()).all()
    if request.method == "POST":
        boleto = Mensalidade(
            cliente_id=int(request.form["cliente_id"]),
            descricao=request.form["descricao"],
            valor=float(request.form["valor"]),
            vencimento=request.form["vencimento"],
            status=request.form["status"],
            codigo_boleto=request.form["codigo_boleto"]
        )
        db.session.add(boleto)
        db.session.commit()
        return redirect(url_for("financeiro.mensalidades"))
    return render_template("cadastrar_boleto.html", clientes=clientes)
