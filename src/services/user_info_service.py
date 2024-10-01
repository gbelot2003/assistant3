# src/services/user_info_service.py

class UserInfoService:
    def __init__(self):
        self.nombre = None
        self.email = None

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def tiene_nombre(self):
        return self.nombre is not None

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def tiene_email(self):
        return self.email is not None