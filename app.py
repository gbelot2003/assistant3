from flask import Flask, render_template, request, jsonify
from src.routes.router import configure_routes
app = Flask(__name__)



# Configurar las rutas
configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
