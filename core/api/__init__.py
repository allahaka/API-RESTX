from flask import Blueprint
from flask_restx import Api
from core.api.users.views import api as ns1

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
          title='Testing',
          version='1.0',
          description='A description',
          )

api.add_namespace(ns1, path='/user')
