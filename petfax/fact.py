from flask import (Blueprint, render_template)
import json

facts = [
    {"name": "Dog", "fact": "Dogs nose prints are unique, much like a person's fingerprint."},
    {"name": "Cat", "fact": "Cats have 230 bones, while humans only have 206"},
    {"name": "Parrot", "fact": "The smallest parrot in the world is three inches long."}
]
bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/')
def show_facts():
    return render_template('facts.html', facts=facts)

@bp.route('/new')
def new_fact():
    return render_template('new.html')