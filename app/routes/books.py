from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.book import Book
from .. import db

books_bp = Blueprint('books', __name__, url_prefix='')


@books_bp.route('/catalogo')
def catalog():
    q = request.args.get('q', '')
    if q:
        books = Book.query.filter((Book.title.ilike(f'%{q}%')) | (Book.author.ilike(f'%{q}%'))).all()
    else:
        books = Book.query.all()
    return render_template('catalogo.html', books=books, q=q)


@books_bp.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)
