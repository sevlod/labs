from flask import Blueprint, render_template, redirect, url_for
from .forms import NameForm
from . import db
from sqlalchemy import text

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        db.session.execute(text("INSERT INTO names (name) VALUES (:name)"), {"name": name})
        db.session.commit()
        return redirect(url_for('main.thank_you', name=name))
    return render_template('index.html', form=form)

@main.route('/thankyou/<name>')
def thank_you(name):
    return f"Thank you, {name}!"