# app.py

from flask import Flask
from src.routes.router import configure_routes
from src.actions.chromadb_action import ChromaDBAction
from src.actions.pdf_processing_action import PDFProcessingService
from src.actions.embedding_processing_action import EmbeddingProcessingAction
from flask_migrate import Migrate
from config import Config
from extensions import db


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# Lista de rutas de archivos PDF
pdf_paths = [
    "files/encomiendas.pdf",
    # Agrega más rutas de archivos PDF aquí
]

# Procesar cada PDF al iniciar la aplicación
for pdf_path in pdf_paths:
    try:
        text = PDFProcessingService().extract_text_from_pdf(pdf_path)
        chunks = PDFProcessingService().split_text_into_chunks(text)
        chunks_with_embeddings = [(chunk, EmbeddingProcessingAction().get_embedding_for_chunk(chunk)) for chunk in chunks]
        ChromaDBAction().store_chunks_in_chromadb(chunks_with_embeddings, pdf_path)
    except Exception as e:
        print(f"Error procesando el PDF {pdf_path}: {e}")


# Configurar las rutas
configure_routes(app)

# Iniciar el servidor
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)