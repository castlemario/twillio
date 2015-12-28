from airtng_flask.models import app_db

db = app_db()


class VacationProperty(db.Model):
    __tablename__ = "vacation_properties"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

    host_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    host = db.relationship("Host", back_populates="vacation_properties")
    reservations = db.relationship("Reservation", back_populates="vacation_property")

    def __init__(self, name, image_url, host):
        self.name = name
        self.image_url = image_url
        self.host = host

    def __repr__(self):
        return '<VacationProperty %r %r>' % self.id, self.name
