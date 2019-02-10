from flask import flash, redirect, url_for, render_template, request
from sqlalchemy import desc, or_

from forms.book import DriftForm
from libs.email import send_mail
from models.base import db
from models.book import Book
from models.drift import Drift
from models.gift import Gift
from models.user import User
from view_models.book import BookViewModel
from view_models.drift import DriftViewModel
from . import web
from flask_login import login_required, current_user


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)

    if current_gift.is_yourself_gift(current_user.id):
        flash('这本书是你自己的^_^, 不能向自己索要书籍噢')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))
    can = current_user.can_send_drift()
    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)

    form = DriftForm(request.form)
    if request.method == 'POST' and form.validate():
        save_drift(form, current_gift)
        send_user = User.query.get(current_gift.uid)
        send_mail(send_user.email, '有人想要一本书', 'email/get_gift.html', wisher=current_user, gift=current_gift)
        return redirect(url_for('web.pending'))
    gifter = User.query.get(current_gift.uid).summary
    return render_template('drift.html', gifter=gifter, user_beans=current_user.beans, form=form)


@web.route('/pending')
@login_required
def pending():
    drifts = Drift.query.filter(
        or_(Drift.requester_id == current_user.id,
            Drift.gifter_id == current_user.id)).order_by(desc(Drift.create_time)).all()
    view_model = DriftViewModel.pending(drifts)
    return render_template('pending.html', drifts=view_model)


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass


def save_drift(drift_form, current_gift):
    with db.auto_commit():
        drift = Drift()
        drift_form.populate_obj(drift)
        drift.gift_id = current_gift.id
        drift.requester_id = current_user.id
        drift.requester_nickname = current_user.nickname
        send_user = User.query.get(current_gift.uid)
        drift.gifter_nickname = send_user.nickname
        drift.gifter_id = send_user.id

        book = BookViewModel(current_gift.book)
        drift.book_title = book.title
        drift.book_author = book.author
        drift.book_img = book.image
        drift.isbn = book.isbn

        current_user.beans -= 1

        db.session.add(drift)
