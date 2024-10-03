from extensions import db

class Delivery(db.Model):
    __tablename__ = 'deliveries'

    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id'), nullable=False)
    package = db.relationship('Package', backref=db.backref('deliveries', lazy=True))
    delivery_time = db.Column(db.DateTime, nullable=False)  # Hora de entrega
    extra_charge = db.Column(db.Float, nullable=True)  # Cargo extra por distancia
    status = db.Column(db.String(50), nullable=False, default='scheduled')  # Estado de la entrega