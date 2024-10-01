# src/actions/name_action.py

# src/actions/name_action.py
from src.extractors.name_extractor import NombreExtractor
from src.repos.contact_repo import ContactRepo

class NameAction:
    def __init__(self, contacto, messages):
        self.contacto = contacto
        self.messages = messages

    def process_name(self):
        messages = []
        # Si el contacto tiene un nombre, usarlo en la conversación
        if self.contacto.nombre:
            messages.append({"role": "assistant", "content": f"El usuario se llama y llamalo {self.contacto.nombre}."})
            return messages
        else:
            extraerNombre = NombreExtractor().extraer_nombre(self.contacto.prompt)
            # grabar nombre en base de datos
            if extraerNombre:
                ContactRepo().actualizar_contacto(self.contacto.id, nombre=extraerNombre)
                messages.append({"role": "system", "content": f"El usuario se llama y llamalo {extraerNombre}."})
                return messages