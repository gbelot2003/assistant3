# app.py

from flask import Flask
from src.routes.router import configure_routes
from flask_migrate import Migrate
from config import Config
from extensions import db


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


# Configurar las rutas
configure_routes(app)

# Iniciar el servidor
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)