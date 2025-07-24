# resources/user_list.py
from flask_restful import Resource, reqparse
from api_response import ApiResponse
from resources.user import users, next_id

class UserListResource(Resource):
    def get(self):
        return ApiResponse("success", data=users), 200

    def post(self):
        global next_id
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()

        if any(u['email'] == args['email'] for u in users):
            return ApiResponse("error", "Email already exists"), 400

        new_user = {
            "id": next_id,
            "name": args['name'],
            "email": args['email']
        }
        users.append(new_user)
        next_id += 1

        return ApiResponse("success", "User created", new_user), 201
