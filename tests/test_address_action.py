import unittest
from src.actions.address_action import AddressAction
from src.repos.contact_repo import ContactRepo
from src.models.contact_model import Contact

class TestAddressAction(unittest.TestCase):

    def setUp(self):
        # Crear un contacto de prueba
        self.contacto = Contact(id=1, nombre="Juan", telefono="123456789", direccion=None, email="juan@example.com")
        self.prompt = "Quiero enviar una caja a mi casa en Calle Principal 123, Ciudad."

    def test_process_address_with_valid_address(self):
        # Crear una instancia de AddressAction
        address_action = AddressAction(self.contacto, self.prompt)

        # Procesar la dirección
        result = address_action.process_address()

        # Verificar que la dirección se haya extraído correctamente
        self.assertEqual(result["role"], "assistant")
        self.assertIn("Calle Principal 123, Ciudad", result["content"])

        # Verificar que la dirección se haya guardado en la base de datos
        updated_contacto = ContactRepo.obtener_contacto_por_telefono(self.contacto.telefono)
        self.assertEqual(updated_contacto.direccion, "Calle Principal 123, Ciudad")

    def test_process_address_with_no_address(self):
        # Crear una instancia de AddressAction con un prompt sin dirección
        address_action = AddressAction(self.contacto, "Quiero enviar una caja a mi casa.")

        # Procesar la dirección
        result = address_action.process_address()

        # Verificar que se haya solicitado la dirección
        self.assertEqual(result["role"], "system")
        self.assertEqual(result["content"], "Por favor, proporciona tu dirección para un mejor servicio.")

        # Verificar que la dirección no se haya guardado en la base de datos
        updated_contacto = ContactRepo.obtener_contacto_por_telefono(self.contacto.telefono)
        self.assertIsNone(updated_contacto.direccion)

if __name__ == "__main__":
    unittest.main()