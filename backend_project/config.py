import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # may be None
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///app.db"


class TestingConfig(Config):
    """Config for running tests."""

    pass


class ProductionConfig(Config):
    """Config for production deployment."""

    pass
