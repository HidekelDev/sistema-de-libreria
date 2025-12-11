"""Script para poblar la base de datos con datos de ejemplo.

Uso:
    python3 scripts/seed.py
"""
import os
import sys

from app import create_app, db
from app.models.user import User
from app.models.book import Book


def run():
    app = create_app()
    with app.app_context():
        # crear tablas
        db.create_all()

        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@example.com', is_admin=True)
            admin.set_password('adminpass')
            db.session.add(admin)

        # algunos libros
        sample_books = [
            ('Cien años de soledad', 'Gabriel García Márquez', '978-0307474728'),
            ('El Principito', 'Antoine de Saint-Exupéry', '978-0156012195'),
            ('Introducción a Algoritmos', 'Cormen, Leiserson, Rivest, Stein', '978-0262033848')
        ]
        for title, author, isbn in sample_books:
            if not Book.query.filter_by(isbn=isbn).first():
                b = Book(title=title, author=author, isbn=isbn, total_copies=3, available_copies=3)
                db.session.add(b)

        db.session.commit()
        print('Seed completado')


if __name__ == '__main__':
    run()
