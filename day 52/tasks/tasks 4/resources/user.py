# resources/user.py
from flask_restful import Resource, reqparse
from api_response import ApiResponse

# Dummy in-memory storage
users = []
next_id = 1

class UserResource(Resource):
    def get(self, user_id):
        user = next((u for u in users if u['id'] == user_id), None)
        if user:
            return ApiResponse("success", data=user), 200
        return ApiResponse("error", "User not found"), 404

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()

        for user in users:
            if user['id'] == user_id:
                user['name'] = args['name']
                user['email'] = args['email']
                return ApiResponse("success", "User updated", user), 200

        return ApiResponse("error", "User not found"), 404

    def delete(self, user_id):
        global users
        user = next((u for u in users if u['id'] == user_id), None)
        if user:
            users = [u for u in users if u['id'] != user_id]
            return ApiResponse("success", f"User {user_id} deleted"), 200
        return ApiResponse("error", "User not found"), 404
