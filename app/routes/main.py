from flask import Blueprint, render_template
from flask_login import login_required
from ..models import Cliente, Mensalidade

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return render_template("home.html")

@bp.route("/dashboard")
@login_required
def dashboard():
    total_clientes = Cliente.query.count()
    total_mensalidades = Mensalidade.query.count()
    pagas = Mensalidade.query.filter_by(status="Pago").count()
    pendentes = Mensalidade.query.filter_by(status="Pendente").count()
    atrasadas = Mensalidade.query.filter_by(status="Atrasado").count()
    return render_template(
        "dashboard.html",
        total_clientes=total_clientes,
        total_mensalidades=total_mensalidades,
        pagas=pagas,
        pendentes=pendentes,
        atrasadas=atrasadas
    )
