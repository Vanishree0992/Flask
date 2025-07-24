# app.py
from flask import Flask
from flask_restful import Api
from resources.user import UserResource
from resources.user_list import UserListResource

app = Flask(__name__)
api = Api(app)

# Resource routes
api.add_resource(UserListResource, '/api/users')
api.add_resource(UserResource, '/api/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
