from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from datetime import datetime
import os

# Starting Flask App
app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

# Initializing Flask Bootstrap
bootstrap = Bootstrap5()
bootstrap.init_app(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.context_processor
def inject_variables():
    cur_year = datetime.now().year
    return dict(year=cur_year)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
