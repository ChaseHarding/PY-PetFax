from flask import (Blueprint, render_template, request)
import json

# pets = json.load(open('pets.json'))
bp = Blueprint('pet', __name__, url_prefix="/pets")

# print(pets)

def load_pets():
    with open('pets.json') as f:
        return json.load(f)

@bp.route('/')
def index():
    if request.method == 'GET':
        pets = json.load(open('pets.json'))
        return render_template('pets/index.html', pets=pets)
    elif request.method == 'POST':
        print(request.form)
        return 'Thanks for submitting a fun fact!'

@bp.route('/<int:id>')
def show(id):
    pets = load_pets()
    # pet = pets[id - 1]
    pet = next((pet for pet in pets if pet['pet_id'] == str(id)), None)
    if pet is None:
        return "Pet not found", 404
    return render_template('pets/show.html', pet=pet)