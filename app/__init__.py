from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_recaptcha import ReCaptcha
from flask_nav import Nav
from flask_nav.elements import *

import random
import string
from datetime import timedelta

import os

# Init & Config
app = Flask(__name__, instance_relative_config=True)
app.secret_key=''.join(random.SystemRandom().choice(string.hexdigits) for _ in range(30))
#By default in Flask, permanent_session_lifetime is set to 31 days
#app.permanent_session_lifetime = timedelta(minutes=30)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Init modules
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
recaptcha = ReCaptcha(app=app)

# Other Config
app.url_map.strict_slashes = False


# Cache busting
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



from app import views
