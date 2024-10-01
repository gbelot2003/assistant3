import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SystemMessage:

    def handle_request(self, prompt):
        print(f"Usuario: {prompt}")

        # Definir el prompt del usuario
        messages = []

        # Agregar el mensaje actual del usuario
        messages.append({"role": "user", "content": prompt})


        # Enviar los mensajes a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=150, temperature=0.1  # type: ignore
        )
        
        # Obtener la respuesta generada por el modelo
        respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore

        # Imprimir la respuesta generada por el modelo
        print(f"GPT: {respuesta_modelo}")

        return respuesta_modelo