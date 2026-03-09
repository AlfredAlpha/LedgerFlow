from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from ..models import Cliente
from .. import db

bp = Blueprint("clientes", __name__, url_prefix="/clientes")

@bp.route("/")
@login_required
def lista():
    clientes = Cliente.query.order_by(Cliente.id.desc()).all()
    return render_template("clientes.html", clientes=clientes)

@bp.route("/novo", methods=["GET", "POST"])
@login_required
def novo():
    if request.method == "POST":
        cliente = Cliente(
            nome=request.form["nome"],
            empresa=request.form["empresa"],
            cidade=request.form["cidade"],
            email=request.form.get("email"),
            telefone=request.form.get("telefone"),
            documento=request.form.get("documento")
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for("clientes.lista"))
    return render_template("cadastrar_cliente.html")
