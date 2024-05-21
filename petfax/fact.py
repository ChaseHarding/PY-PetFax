from flask import (Blueprint, render_template)
import json

bp = Blueprint('fact', __name__, url_prefix="/facts")
fact = json.load(open('facts.json'))

# Create a route for /facts and a route for /facts/new

@bp.route('/new')
def index():
    return render_template('new.html', fact=fact)