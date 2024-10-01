# config.py

import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey!")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False