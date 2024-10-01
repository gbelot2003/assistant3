# src/routes/twilio.py
from flask import request, jsonify
from src.services.openai_service import OpenAIService

def configure_twilio_routes(app):
    @app.route('/api/twilio', methods=['POST'])
    def twilio_webhook():
        try:
            # Obtener datos desde mensajes de API
            message_body = request.form.get('Body')
            from_number = request.form.get('From')

            if not message_body or not from_number:
                return jsonify({"error": "Missing required parameters"}), 400

            response = OpenAIService().handle_request(message_body, from_number)

            # Devolver la respuesta a Twilio
            return jsonify({"message": response})
        except Exception as e:
            return jsonify({"error": str(e)}), 500