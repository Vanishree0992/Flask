from flask import Flask, request
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# In-memory database
users = []
next_id = 1

# Utilities
def find_user(user_id):
    return next((user for user in users if user["id"] == user_id), None)

# Resource: All Users
class UserList(Resource):
    def get(self):
        return {"status": "success", "users": users}, 200

    def post(self):
        global next_id
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return {"status": "error", "message": "Missing name or email"}, 400
        
        if any(u['email'] == data['email'] for u in users):
            return {"status": "error", "message": "Email already exists"}, 400
        
        new_user = {
            "id": next_id,
            "name": data["name"],
            "email": data["email"]
        }
        users.append(new_user)
        next_id += 1
        return {"status": "success", "user": new_user}, 201

# Resource: Single User
class User(Resource):
    def get(self, user_id):
        user = find_user(user_id)
        if user:
            return {"status": "success", "user": user}, 200
        return {"status": "error", "message": "User not found"}, 404

    def put(self, user_id):
        data = request.get_json()
        user = find_user(user_id)
        if not user:
            return {"status": "error", "message": "User not found"}, 404

        if not data or 'name' not in data or 'email' not in data:
            return {"status": "error", "message": "Missing name or email"}, 400

        if any(u["email"] == data["email"] and u["id"] != user_id for u in users):
            return {"status": "error", "message": "Email already exists"}, 400

        user["name"] = data["name"]
        user["email"] = data["email"]
        return {"status": "success", "user": user}, 200

    def delete(self, user_id):
        global users
        user = find_user(user_id)
        if not user:
            return {"status": "error", "message": "User not found"}, 404

        users = [u for u in users if u["id"] != user_id]
        return {"status": "success", "message": f"User {user_id} deleted"}, 200

# Resource: Clear All Users
class ClearUsers(Resource):
    def delete(self):
        global users, next_id
        users = []
        next_id = 1
        return {"status": "success", "message": "All users cleared"}, 200

# API routes with /api prefix
api.add_resource(UserList, "/api/users")
api.add_resource(User, "/api/users/<int:user_id>")
api.add_resource(ClearUsers, "/api/users/clear")

# Run the API
if __name__ == '__main__':
    app.run(debug=True)
