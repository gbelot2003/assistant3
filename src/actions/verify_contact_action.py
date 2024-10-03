from src.repos.contact_repo import ContactRepo

class VerifyContactAction:
    def __init__(self):
        pass

    @staticmethod
    def verificar_contacto(user_id):
        print("Verificando contacto...")
        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = ContactRepo.obtener_contacto_por_telefono(user_id)

        if not contacto:
            # Si no existe, crear un nuevo contacto con el número de teléfono
            contacto = ContactRepo.crear_contacto(telefono=user_id)

        return contacto

    @staticmethod
    def actualizar_contacto(contacto_id, nombre=None, telefono=None, direccion=None, email=None):
        # Obtener el contacto existente
        contacto = ContactRepo.obtener_contacto_por_telefono(contacto_id)

        if contacto:
            # Actualizar solo los campos que no son None
            if nombre is not None:
                contacto.nombre = nombre
            if telefono is not None:
                contacto.telefono = telefono
            if direccion is not None:
                contacto.direccion = direccion
            if email is not None:
                contacto.email = email

            # Guardar los cambios en la base de datos
            ContactRepo.actualizar_contacto(contacto.id, contacto.nombre, contacto.telefono, contacto.direccion, contacto.email)

        return contacto