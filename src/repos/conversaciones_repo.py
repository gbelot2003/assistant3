from extensions import db
from src.models.conversacion_model import Conversacion

class ConversacionRepo:
    @staticmethod
    def crear_conversacion(user_message, bot_response, user_id):
        nueva_conversacion = Conversacion(user_message=user_message, bot_response=bot_response, user_id=user_id)
        db.session.add(nueva_conversacion)
        db.session.commit()
        return nueva_conversacion

    @staticmethod
    def obtener_conversaciones_por_user_id(user_id):
        return Conversacion.query.filter_by(user_id=user_id).all()

    @staticmethod
    def obtener_todas_conversaciones():
        return Conversacion.query.all()

    @staticmethod
    def eliminar_conversacion(conversacion_id):
        conversacion = Conversacion.query.filter_by(id=conversacion_id).first()
        if conversacion:
            db.session.delete(conversacion)
            db.session.commit()
        return conversacion