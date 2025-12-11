from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models.book import Book
from ..models.loan import Loan

loans_bp = Blueprint('loans', __name__, url_prefix='')


@loans_bp.route('/borrow/<int:book_id>')
@login_required
def borrow(book_id):
    book = Book.query.get_or_404(book_id)
    if book.available_copies < 1:
        flash('No hay copias disponibles')
        return redirect(url_for('books.catalog'))
    loan = Loan(user_id=current_user.id, book_id=book.id)
    book.available_copies -= 1
    db.session.add(loan)
    db.session.commit()
    flash('Préstamo realizado')
    return redirect(url_for('books.catalog'))


@loans_bp.route('/return/<int:loan_id>')
@login_required
def return_book(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    if loan.user_id != current_user.id and not current_user.is_admin:
        flash('No autorizado')
        return redirect(url_for('books.catalog'))
    if not loan.returned:
        loan.mark_returned()
        loan.book.available_copies += 1
        db.session.commit()
        flash('Libro devuelto')
    return redirect(url_for('books.catalog'))
