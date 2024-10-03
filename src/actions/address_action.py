# src/actions/address_action.py

from src.repos.contact_repo import ContactRepo

class AddressAction:
    def __init__(self, contacto, prompt):
        self.contacto = contacto
        self.prompt = prompt

    def process_address(self):
        # Aquí puedes implementar la lógica para extraer la dirección del prompt
        # Por ejemplo, usando expresiones regulares o un extractor de direcciones
        address = self.extract_address(self.prompt)
        if address:
            ContactRepo.actualizar_contacto(self.contacto.id, direccion=address)
            print("La dirección del usuario ha sido registrada en la base de datos.")
            return {"role": "assistant", "content": f"La dirección del usuario ha sido registrada como: {address}."}
        else:
            return {"role": "system", "content": "Por favor, proporciona tu dirección para un mejor servicio."}

    def extract_address(self, text):
        # Implementa aquí la lógica para extraer la dirección del texto
        # Esto puede ser una expresión regular o un servicio externo
        # Por simplicidad, aquí se asume que la dirección está en el texto
        return text.split("dirección:")[-1].strip() if "dirección:" in text else None