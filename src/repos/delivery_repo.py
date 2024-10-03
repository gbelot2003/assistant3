from extensions import db
from src.models.delivery_model import Delivery

class DeliveryRepo:
    @staticmethod
    def create_delivery(package_id, delivery_time, extra_charge=None):
        new_delivery = Delivery(package_id=package_id, delivery_time=delivery_time, extra_charge=extra_charge)
        db.session.add(new_delivery)
        db.session.commit()
        return new_delivery

    @staticmethod
    def get_delivery_by_id(delivery_id):
        return Delivery.query.filter_by(id=delivery_id).first()