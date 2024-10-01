import os
from openai import OpenAI
from dotenv import load_dotenv
from src.extractors.name_extractor import NombreExtractor
from src.actions.name_action import NameAction
from src.actions.verify_contact_action import VerifyContactAction
from src.services.user_info_service import UserInfoService
from src.repos.conversaciones_repo import ConversacionRepo
from src.repos.contact_repo import ContactRepo


load_dotenv(override=True)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SystemMessage:

    def handle_request(self, prompt, user_id):
        print(f"system: {prompt}")

        # Definir el prompt del usuario
        messages = []

        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = VerifyContactAction().verificar_contacto(user_id)

        # Procesar el nombre del contacto
        name_action = NameAction(contacto, messages)
        messages = name_action.process_name()

        # Agregar el mensaje actual del usuario
        messages.append({"role": "user", "content": prompt})


        # Enviar los mensajes a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=150, temperature=0.1  # type: ignore
        )
        
        # Obtener la respuesta generada por el modelo
        respuesta_modelo = response.choices[0].message.content.strip()  # type: ignore

    
        # Guardar la conversión del modelo en la base de datos
        ConversacionRepo().crear_conversacion(prompt, respuesta_modelo, user_id)

        return respuesta_modelo