from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'my_catalog'}
app.debug = True
db = MongoEngine(app)

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

""" with app.app_context():
    db.create_all() """