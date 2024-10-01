# src/routes/twilio.py
from flask import request, jsonify
from src.services.openai_service import OpenAIService

def configure_twilio_routes(app):
    # Ruta para el webhook
    @app.route('/api/twilio', methods=['POST'])
    def twilio_webhook():
        
        # Obtener datos desde mensajes de API
        message_body = request.form.get('Body')
        from_number = request.form.get('From')

        response = OpenAIService().handle_request(message_body)

         # Devolver la respuesta a Twilio
        return jsonify({"message": response})