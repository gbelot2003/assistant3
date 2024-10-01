# src/routes/router.py

from flask import render_template
from src.routes.api import configure_api_routes
from src.routes.twilio import configure_twilio_routes
from src.services.openai_service import OpenAIService
from dotenv import load_dotenv

load_dotenv(override=True)

def configure_routes(app):
    
    # Ruta para el webhook

    configure_twilio_routes(app)

    configure_api_routes(app)

    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")
    
  