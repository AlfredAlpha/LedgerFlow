from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Faça login para acessar o sistema."

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .models import Colaborador

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(Colaborador, int(user_id))

    from .routes.main import bp as main_bp
    from .routes.auth import bp as auth_bp
    from .routes.clientes import bp as clientes_bp
    from .routes.financeiro import bp as financeiro_bp
    from .routes.api import bp as api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(financeiro_bp)
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app
