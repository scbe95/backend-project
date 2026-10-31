from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from .extensions import db, migrate
from .config import DevelopmentConfig, TestingConfig, ProductionConfig

def create_app(config_name):
    app = Flask(__name__)

    config_map = {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }

    config_class = config_map.get(config_name, DevelopmentConfig)
    app.config.from_object(config_class)

    print("DB URI at startup:", app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main_bp
    app.register_blueprint(main_bp)

    # we'll use config_name later; for now we just accept it
    return app
