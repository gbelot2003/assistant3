from src.actions.address_action import AddressAction
from src.actions.email_action import EmailAction
from src.actions.conversation_history_action import ConversationHistoryAction
from src.actions.verify_contact_action import VerifyContactAction
from src.repos.chromadb_repo import ChromaDBRepo
from src.actions.name_action import NameAction

class ActionHandleService:
    def __init__(self, user_id, prompt):
        self.user_id = user_id
        self.prompt = prompt
        self.messages = []

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


        return self.messages