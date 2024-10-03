# src/actions/address_action.py

import spacy
from src.repos.contact_repo import ContactRepo

# Cargar el modelo de SpaCy para español
nlp = spacy.load("es_core_news_sm")

class AddressAction:
    def __init__(self, contacto, prompt):
        self.contacto = contacto
        self.prompt = prompt

    def process_address(self):
        # Aquí puedes implementar la lógica para extraer la dirección del prompt
        address = self.extract_address(self.prompt)
        if address:
            print(f"Extraído: {address}")
            ContactRepo.actualizar_contacto(self.contacto.id, direccion=address)
            return {"role": "assistant", "content": f"La dirección del usuario ha sido registrada como: {address}."}
        else:
            return {"role": "system", "content": "Por favor, proporciona tu dirección para un mejor servicio."}

    def extract_address(self, text):
        # Procesar el texto con SpaCy
        doc = nlp(text)
        
        # Buscar entidades de tipo "LOC" (localización) que podrían ser direcciones
        addresses = [ent.text for ent in doc.ents if ent.label_ == "LOC"]
        
        # Si se encuentra alguna dirección, devolver la primera encontrada
        if addresses:
            return addresses[0]
        else:
            return None
