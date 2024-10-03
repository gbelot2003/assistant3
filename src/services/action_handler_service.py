from src.actions.conversation_history_action import ConversationHistoryAction
from src.actions.verify_contact_action import VerifyContactAction
from src.repos.chromadb_repo import ChromaDBRepo
from src.actions.name_action import NameAction
from src.actions.address_action import AddressAction
from src.actions.email_action import EmailAction
from src.actions.schedule_delivery_action import ScheduleDeliveryAction
from src.services.intent_service import IntentService
from geopy.geocoders import Nominatim
from config import Config

class ActionHandleService:
    def __init__(self, user_id, prompt):
        self.user_id = user_id
        self.prompt = prompt
        self.messages = []
        self.context = {
            "package_type": None,
            "delivery_time": None,
            "address": None,
            "email": None,
            "phone": None,
        }
        self.geolocator = Nominatim(user_agent="delivery_scheduler")
        self.box_types = Config.BOX_TYPES

    def handle_actions(self):
        # Verificar si el usuario tiene un número de teléfono en la base de datos
        contacto = VerifyContactAction().verificar_contacto(self.user_id)

        # Buscar fragmentos relevantes en ChromaDB
        chromadb_repo = ChromaDBRepo()
        relevant_chunks = chromadb_repo.buscar_fragmentos_relevantes(self.prompt)
        if relevant_chunks:
            self.messages.append(relevant_chunks)

        # Buscar historial de conversación
        conversation_history_action = ConversationHistoryAction()
        chat_history_messages = conversation_history_action.compilar_conversacion(self.user_id)
        self.messages.extend(chat_history_messages)

        # Procesar el nombre del contacto
        name_action = NameAction(contacto, self.prompt)
        name_message = name_action.process_name()
        if name_message:
            self.messages.append(name_message)

        # Procesar la dirección del contacto
        address_action = AddressAction(contacto, self.prompt)
        address_message = address_action.process_address()
        if address_message:
            self.messages.append(address_message)

        # Procesar el email del contacto
        email_action = EmailAction(contacto, self.prompt)
        email_message = email_action.process_email()
        if email_message:
            self.messages.append(email_message)

        # Detectar intent
        intent_service = IntentService(self.prompt)
        intent, data = intent_service.detect_intent()

        if intent == "schedule_delivery":
            self.messages.append({"role": "system", "content": "Por favor, proporciona el tipo de caja, la hora de entrega, la dirección, el email y el teléfono."})
        elif intent == "provide_package_type":
            package_type = data[0].lower()
            if package_type in self.box_types:
                self.context["package_type"] = self.box_types[package_type]
                self.messages.append({"role": "system", "content": f"Tipo de caja registrado: {self.context['package_type']}"})
            else:
                self.messages.append({"role": "system", "content": "Tipo de caja no válido. Por favor, selecciona uno de los siguientes tipos: small, medium, large, extra_large, extra_extra_large."})
        elif intent == "provide_delivery_time":
            self.context["delivery_time"] = data[0]
            self.messages.append({"role": "system", "content": f"Hora de entrega registrada: {data[0]}"})
        elif intent == "provide_address":
            self.context["address"] = data[0]
            self.messages.append({"role": "system", "content": f"Dirección registrada: {data[0]}"})
        elif intent == "provide_email":
            self.context["email"] = data[0]
            self.messages.append({"role": "system", "content": f"Email registrado: {data[0]}"})
        elif intent == "provide_phone":
            self.context["phone"] = data[0]
            self.messages.append({"role": "system", "content": f"Teléfono registrado: {data[0]}"})

        # Verificar si se tiene toda la información necesaria para agendar la entrega
        if all(self.context.values()):
            # Obtener las coordenadas de la dirección del cliente
            customer_coords = self.get_coordinates_from_address(self.context["address"])
            if not customer_coords:
                self.messages.append({"role": "system", "content": "No se pudo obtener las coordenadas de la dirección."})
            else:
                # Agendar la entrega
                schedule_delivery_action = ScheduleDeliveryAction(
                    self.user_id,
                    self.context["package_type"],
                    self.context["delivery_time"],
                    self.context["address"]
                )
                delivery_message = schedule_delivery_action.schedule_delivery()
                if delivery_message:
                    self.messages.append(delivery_message)
        else:
            # Verificar si el contacto ya tiene un número de teléfono registrado
            if not contacto.telefono:
                self.messages.append({"role": "system", "content": "Por favor, proporciona tu número de teléfono."})

        return self.messages

    def get_coordinates_from_address(self, address):
        try:
            location = self.geolocator.geocode(address)
            if location:
                return (location.latitude, location.longitude)
            return None
        except Exception as e:
            print(f"Error obteniendo coordenadas: {e}")
            return None