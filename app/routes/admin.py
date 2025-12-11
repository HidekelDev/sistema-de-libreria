from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models.book import Book
from .. import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(func):
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Acceso denegado')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


@admin_bp.route('/')
@login_required
@admin_required
def index():
    books = Book.query.all()
    return render_template('admin/index.html', books=books)


@admin_bp.route('/books/new', methods=['GET', 'POST'])
@login_required
@admin_required
def new_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')
        copies = int(request.form.get('copies', 1))
        b = Book(title=title, author=author, isbn=isbn, total_copies=copies, available_copies=copies)
        db.session.add(b)
        db.session.commit()
        flash('Libro agregado')
        return redirect(url_for('admin.index'))
    return render_template('admin/new_book.html')
