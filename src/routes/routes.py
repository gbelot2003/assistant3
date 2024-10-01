# src/routes/routes.py

import os
import requests
from flask import render_template, jsonify, request
from src.services.openai_service import OpenAIService
from dotenv import load_dotenv

load_dotenv(override=True)

def configure_routes(app):
    
    # Ruta para el home
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route('/api/send_message', methods=['POST'])
    def send_message():
        data = request.json
        target_url = data.get('url')
        message_body = data.get('message', 'Este es un mensaje simulado desde Twilio')
        from_number = data.get('from_number', '+14155551234')  # Número simulado del remitente por defecto

        # Simulando el POST de Twilio
        simulated_twilio_post = {
            "SmsMessageSid": "SM12345678901234567890123456789012",
            "NumMedia": "0",
            "SmsSid": "SM12345678901234567890123456789012",
            "SmsStatus": "received",
            "Body": message_body,  # Utiliza la variable message_body definida previamente o asigna un mensaje manualmente
            "To": os.getenv("TWILIO_NUMBER"),  # Número de tu cuenta Twilio para pruebas
            "NumSegments": "1",
            "MessageSid": "SM12345678901234567890123456789012",
            "AccountSid": os.getenv("TWILIO_ACCOUNT_SID"),  # SID de cuenta simulado
            "From": from_number,  # Número simulado del remitente, configurable desde la interfaz
            "ApiVersion": "2010-04-01",
            "ProfileName": "Twilio Simulator",  # Nombre del perfil simulado
            "WaId": from_number.replace('+', ''),  # ID simulado del usuario en WhatsApp
            "ChannelPrefix": "whatsapp",  # Canal desde el cual proviene el mensaje
            "Type": "TextMessage"  # Tipo de mensaje
        }

        # Envío del POST a la URL proporcionada
        try:
            response = requests.post(target_url, data=simulated_twilio_post)
            response_data = response.json()  # Asegurarse de que la respuesta sea un JSON
            return jsonify({"status": "success", "response": response_data})
        except Exception as e:
            return jsonify({"status": "error", "response": str(e)})


    # Ruta para el webhook
    @app.route('/api/twilio', methods=['POST'])
    def twilio_webhook():
        
        # Obtener datos desde mensajes de API
        message_body = request.form.get('Body')
        from_number = request.form.get('From')

        response = OpenAIService().handle_request(message_body)

         # Devolver la respuesta a Twilio
        return jsonify({"message": response})