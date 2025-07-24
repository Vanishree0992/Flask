from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest, NotFound
import re

app = Flask(__name__)
api = Api(app)

tickets = []
ticket_id_counter = 1

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
VALID_PRIORITIES = {"Low", "Medium", "High"}

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email)

class TicketListResource(Resource):
    def get(self):
        return {'tickets': tickets}, 200

    def post(self):
        global ticket_id_counter
        data = request.get_json()

        if not data or 'email' not in data or 'issue' not in data or 'priority' not in data:
            raise BadRequest("Fields 'email', 'issue', and 'priority' are required.")

        if not is_valid_email(data['email']):
            raise BadRequest("Invalid email format.")

        if data['priority'] not in VALID_PRIORITIES:
            raise BadRequest("Priority must be one of: Low, Medium, High.")

        new_ticket = {
            'id': ticket_id_counter,
            'email': data['email'],
            'issue': data['issue'],
            'priority': data['priority'],
            'status': 'Open'
        }
        tickets.append(new_ticket)
        ticket_id_counter += 1
        return {'message': 'Ticket submitted successfully', 'ticket': new_ticket}, 201

class TicketResource(Resource):
    def get(self, id):
        ticket = next((t for t in tickets if t['id'] == id), None)
        if not ticket:
            raise NotFound("Ticket not found.")
        return ticket, 200

    def put(self, id):
        ticket = next((t for t in tickets if t['id'] == id), None)
        if not ticket:
            raise NotFound("Ticket not found.")

        ticket['status'] = 'Closed'
        return {'message': 'Ticket closed', 'ticket': ticket}, 200

    def delete(self, id):
        global tickets
        ticket = next((t for t in tickets if t['id'] == id), None)
        if not ticket:
            raise NotFound("Ticket not found.")
        tickets = [t for t in tickets if t['id'] != id]
        return {'message': f'Ticket with id {id} deleted.'}, 200

# Register endpoints
api.add_resource(TicketListResource, '/tickets')
api.add_resource(TicketResource, '/tickets/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
