# flask
from flask import Blueprint, render_template

# application models
from application.models.test import *
from application.index import db

web = Blueprint('web', __name__)

@web.route('', methods=['GET'])
def index():
    return render_template('index.html')