from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField, EmailField
from wtforms.validators import InputRequired, Length, Email


# # WTForm
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=1)], render_kw={"class": "mb-4"})
    email = EmailField("Email Address", validators=[InputRequired(), Email()], render_kw={"class": "mb-4"})
    subject = StringField("Subject", render_kw={"class": "mb-4"})
    message = TextAreaField("Your Message", validators=[InputRequired(), Length(min=5, max=500)],
                            render_kw={"class": "mb-4"})
    submit = SubmitField("Send Mail", render_kw={'class': 'w-75'})
