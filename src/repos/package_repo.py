from extensions import db
from src.models.package_model import Package

class PackageRepo:
    @staticmethod
    def create_package(type, contact_id):
        new_package = Package(type=type, contact_id=contact_id)
        db.session.add(new_package)
        db.session.commit()
        return new_package

    @staticmethod
    def get_package_by_id(package_id):
        return Package.query.filter_by(id=package_id).first()