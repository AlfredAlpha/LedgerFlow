from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from ..models import Colaborador

bp = Blueprint("auth", __name__)

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip()
        senha = request.form["senha"].strip()
        user = Colaborador.query.filter_by(email=email, senha=senha).first()
        if user:
            login_user(user)
            return redirect(url_for("main.dashboard"))
        return render_template("login.html", erro="E-mail ou senha inválidos.")
    return render_template("login.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
