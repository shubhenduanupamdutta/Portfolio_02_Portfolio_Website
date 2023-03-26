from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from datetime import datetime
from forms import *
import smtplib
from email.message import EmailMessage
import os

# Mail ID and Password from environment
EMAIL_ID = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL = os.environ["EMAIL_TO"]
# Starting Flask App
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

# Initializing Flask Bootstrap
bootstrap = Bootstrap5()
bootstrap.init_app(app)


def send_mail(name, email, subject, message):
    with smtplib.SMTP("smtp.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL_ID, PASSWORD)
        msg = EmailMessage()
        email_body = f"From: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        msg.set_content(email_body)
        msg["Subject"] = "You have a new mail from your portfolio website."
        msg["To"] = TO_EMAIL
        msg["From"] = EMAIL_ID
        connection.send_message(msg)


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
