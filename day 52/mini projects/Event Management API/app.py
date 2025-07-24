from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime

app = Flask(__name__)
api = Api(app)

events = []
event_id_counter = 1

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class EventListResource(Resource):
    def get(self):
        return {'events': events}, 200

    def post(self):
        global event_id_counter
        data = request.get_json()

        if not data or 'name' not in data or 'date' not in data or 'location' not in data:
            raise BadRequest("Name, date, and location are required.")

        if not validate_date_format(data['date']):
            raise BadRequest("Date must be in YYYY-MM-DD format.")

        new_event = {
            'id': event_id_counter,
            'name': data['name'],
            'date': data['date'],
            'location': data['location']
        }
        events.append(new_event)
        event_id_counter += 1
        return new_event, 201

class EventResource(Resource):
    def get(self, id):
        event = next((e for e in events if e['id'] == id), None)
        if not event:
            raise NotFound("Event not found.")
        return event, 200

    def put(self, id):
        data = request.get_json()
        event = next((e for e in events if e['id'] == id), None)
        if not event:
            raise NotFound("Event not found.")

        if 'name' in data:
            event['name'] = data['name']
        if 'date' in data:
            if not validate_date_format(data['date']):
                raise BadRequest("Date must be in YYYY-MM-DD format.")
            event['date'] = data['date']
        if 'location' in data:
            event['location'] = data['location']

        return event, 200

    def delete(self, id):
        global events
        event = next((e for e in events if e['id'] == id), None)
        if not event:
            raise NotFound("Event not found.")
        events = [e for e in events if e['id'] != id]
        return {'message': f'Event with id {id} deleted.'}, 200

# Register routes
api.add_resource(EventListResource, '/events')
api.add_resource(EventResource, '/events/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
