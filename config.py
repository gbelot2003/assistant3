# config.py

import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey!")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Definir los tipos de cajas
    BOX_TYPES = {
        "small": "24\"x18\"x18\"",
        "medium": "24\"x24\"x18\"",
        "large": "24\"x24\"x24\"",
        "extra_large": "26\"x26\"x28\"",
        "extra_extra_large": "28\"x28\"x34\""
    }