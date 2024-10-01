# src/actions/name_action.py
from src.extractors.name_extractor import NombreExtractor
from src.repos.contact_repo import ContactRepo
import logging

class NameAction:
    def __init__(self, contacto, prompt):
        self.contacto = contacto
        self.prompt = prompt

    def process_name(self):
        message = None
        # Si el contacto tiene un nombre, usarlo en la conversación
        if self.contacto.nombre:
            message = {"role": "assistant", "content": f"El usuario se llama y llamalo {self.contacto.nombre}."}
        else:
            logging.debug("Nombre no encontrado, intentando extraer...")
            extraerNombre = NombreExtractor().extraer_nombre(self.prompt)            # grabar nombre en base de datos
            if extraerNombre:
                ContactRepo().actualizar_contacto(self.contacto.id, nombre=extraerNombre)
                message = {"role": "assistant", "content": f"El usuario se llama y llamalo {extraerNombre}."}
            else:
                message = {"role": "assistant", "content": f"El usuario se llama y llamalo {self.contacto.telefono}."}
        return message