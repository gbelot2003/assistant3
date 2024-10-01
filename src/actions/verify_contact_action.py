# src/actions/verify_contact_action.py

from src.repos.contact_repo import ContactRepo

class VerifyContactAction:
    def __init__(self, contact_repo):
        self.contact_repo = contact_repo

    def verificar_contacto(user_id):
        print("Verificando contacto...")
        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = ContactRepo.obtener_contacto_por_telefono(user_id)

        if not contacto:
            # Si no existe, crear un nuevo contacto con el número de teléfono
            contacto = ContactRepo.crear_contacto(telefono=user_id)
            print(f"Nuevo contacto creado: {contacto.telefono}")
        else:
            # Si existe, extraer la información del contacto
            nombre = contacto.nombre
            direccion = contacto.direccion
            email = contacto.email
            print(f"Contacto encontrado: {nombre}, {direccion}, {email}")

        return contacto