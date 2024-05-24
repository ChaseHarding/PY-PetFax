from flask import Flask, render_template
import json

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    def load_pets():
        with open('pets.json') as f:
            return json.load(f)

    @app.route('/')
    def index():
        pets = load_pets()
        return render_template('pets/index.html', pets=pets)

    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    return app