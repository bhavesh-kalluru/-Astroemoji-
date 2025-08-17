import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    # Database
    DB_PATH = os.environ.get("ASTROMOJI_DATABASE",
                             os.path.join(os.getcwd(), "instance", "astromoji.sqlite"))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
