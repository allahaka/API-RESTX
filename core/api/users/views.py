from flask_restx import Resource
import core.db.tasks.users_tasks as users_tasks
from core.api.users.model import user, api


@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(user)
    def get(self):
        return users_tasks.select_all_users()


@api.route('/<int:user_id>')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, user_id):
        return users_tasks.select_user_by_id(user_id)
