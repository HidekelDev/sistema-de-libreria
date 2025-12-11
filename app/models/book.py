from .. import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    isbn = db.Column(db.String(20), unique=True)
    total_copies = db.Column(db.Integer, default=1)
    available_copies = db.Column(db.Integer, default=1)

    loans = db.relationship('Loan', backref='book', lazy=True)
    reservations = db.relationship('Reservation', backref='book', lazy=True)

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'
