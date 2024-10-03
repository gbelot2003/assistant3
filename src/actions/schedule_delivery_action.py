from src.repos.package_repo import PackageRepo
from src.repos.delivery_repo import DeliveryRepo
from src.repos.contact_repo import ContactRepo
from geopy.distance import geodesic

class ScheduleDeliveryAction:
    def __init__(self, user_id, package_type, delivery_time, address):
        self.user_id = user_id
        self.package_type = package_type
        self.delivery_time = delivery_time
        self.address = address

    def schedule_delivery(self):
        # Verificar si el usuario existe
        contact = ContactRepo.obtener_contacto_por_telefono(self.user_id)
        if not contact:
            return {"error": "Contacto no encontrado"}

        # Crear el paquete
        package = PackageRepo.create_package(self.package_type, contact.id)

        # Calcular el cargo extra por distancia
        extra_charge = self.calculate_extra_charge(self.address)

        # Crear la entrega
        delivery = DeliveryRepo.create_delivery(package.id, self.delivery_time, extra_charge)

        return {"message": "Entrega agendada exitosamente", "delivery_id": delivery.id}

    def calculate_extra_charge(self, address):
        # Coordenadas de San Antonio, Texas
        san_antonio_coords = (29.4241219, -98.4936282)

        # Obtener las coordenadas de la dirección del cliente
        # Aquí deberías usar un servicio de geocodificación para obtener las coordenadas de la dirección
        # Por simplicidad, asumimos que ya tienes las coordenadas
        customer_coords = self.get_coordinates_from_address(address)

        # Calcular la distancia entre San Antonio y la dirección del cliente
        distance = geodesic(san_antonio_coords, customer_coords).miles

        # Calcular el cargo extra
        if distance <= 30:
            return 0
        elif distance <= 90:
            return (distance - 30) * 1  # $1 por milla extra
        else:
            return (90 - 30) * 1  # Máximo cargo para distancias mayores a 90 millas

    def get_coordinates_from_address(self, address):
        # Implementa aquí la lógica para obtener las coordenadas de la dirección
        # Puedes usar un servicio de geocodificación como Google Maps API o OpenStreetMap
        # Por simplicidad, aquí se asume que ya tienes las coordenadas
        return (29.4241219, -98.4936282)  # Coordenadas de ejemplo