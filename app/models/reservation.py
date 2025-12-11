from datetime import datetime
from .. import db


class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    reserved_at = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    def cancel(self):
        self.active = False

    def __repr__(self):
        return f'<Reservation user={self.user_id} book={self.book_id} active={self.active}>'
