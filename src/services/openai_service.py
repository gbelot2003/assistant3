# src/services/openai_service.py

from src.services.system_message import SystemMessage


class OpenAIService:

    def __init__(self):
        pass

    def handle_request(self, prompt):
        print(f"Usuario: {prompt}")

        respuesta_modelo = SystemMessage().handle_request(prompt)

        # Imprimir la respuesta generada por el modelo
        print(f"GPT: {respuesta_modelo}")

        return respuesta_modelo