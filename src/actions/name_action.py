# src/actions/name_action.py

from src.extractors.name_extractor import NombreExtractor

class NameAction:

    def __init__(self, user_info_service):
        self.extractor = NombreExtractor()
        self.user_info_service = user_info_service


    def extraer_nombre(self, texto):
        # Intentamos extraer el nombre del texto
        nombre_detectado = self.nombre_extractor.extraer_nombre(texto)
        
        if nombre_detectado:
            self.user_info_service.set_nombre(nombre_detectado)
            return nombre_detectado
        return None