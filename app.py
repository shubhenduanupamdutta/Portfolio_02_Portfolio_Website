from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from datetime import datetime
from forms import *
import os

# Starting Flask App
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

# Initializing Flask Bootstrap
bootstrap = Bootstrap5()
bootstrap.init_app(app)


def send_mail(name, email, subject, message):
    pass


@app.route('/', methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        send_mail(form.name.data, form.email.data, form.subject.data, form.message.data)
    return render_template("index.html", form=form)


@app.context_processor
def inject_variables():
    cur_year = datetime.now().year
    return dict(year=cur_year)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
