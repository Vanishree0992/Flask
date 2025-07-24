from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest
import re

app = Flask(__name__)
api = Api(app)

feedback_list = []

# Simple email regex
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email)

class FeedbackResource(Resource):
    def post(self):
        data = request.get_json()

        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            raise BadRequest("Name, email, and message are required.")

        if not is_valid_email(data['email']):
            raise BadRequest("Invalid email format.")

        feedback = {
            'name': data['name'],
            'email': data['email'],
            'message': data['message']
        }
        feedback_list.append(feedback)

        return {
            'message': 'Thank you for your feedback!',
            'feedback_received': feedback
        }, 201

api.add_resource(FeedbackResource, '/feedback')

if __name__ == '__main__':
    app.run(debug=True)
