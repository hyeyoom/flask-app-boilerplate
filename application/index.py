"""application instances here"""

# flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

# flask app
app = Flask(__name__, static_folder='../front/static', template_folder='../front/templates')

# database
db = SQLAlchemy(app)

# toolbar for debug
toolbar = DebugToolbarExtension(app)