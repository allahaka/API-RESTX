from flask import Flask

from core.api import blueprint
from core.consts import DATABASE_URI

app = Flask(__name__)
app.register_blueprint(blueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.run(debug=True)
