from flask_restx import Namespace, fields

api = Namespace('Users', description='Users')

user = api.model('User', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
    'nickname': fields.String(required=True, description='The cat name'),
    'password': fields.String(required=True, description='The cat name'),
    'joining_date': fields.Date(required=True, description='The cat name')
})
