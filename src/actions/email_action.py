# src/actions/email_action.py

from src.repos.contact_repo import ContactRepo

class EmailAction:
    def __init__(self, contacto, prompt):
        self.contacto = contacto
        self.prompt = prompt

    def process_email(self):
        # Aquí puedes implementar la lógica para extraer el email del prompt
        # Por ejemplo, usando expresiones regulares o un extractor de emails
        email = self.extract_email(self.prompt)
        if email:
            ContactRepo.actualizar_contacto(self.contacto.id, email=email)
            return {"role": "assistant", "content": f"El email del usuario ha sido registrado como: {email}."}
        else:
            return {"role": "system", "content": "Por favor, proporciona tu email para un mejor servicio."}

    def extract_email(self, text):
        # Implementa aquí la lógica para extraer el email del texto
        # Esto puede ser una expresión regular o un servicio externo
        # Por simplicidad, aquí se asume que el email está en el texto
        return text.split("email:")[-1].strip() if "email:" in text else None