from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime

app = Flask(__name__)
api = Api(app)

appointments = []
appointment_id_counter = 1

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

class AppointmentListResource(Resource):
    def get(self):
        return {'appointments': appointments}, 200

    def post(self):
        global appointment_id_counter
        data = request.get_json()

        if not data or 'name' not in data or 'date' not in data or 'service' not in data:
            raise BadRequest("Fields 'name', 'date', and 'service' are required.")

        if not validate_date_format(data['date']):
            raise BadRequest("Date must be in YYYY-MM-DD format.")

        appointment = {
            'id': appointment_id_counter,
            'name': data['name'],
            'date': data['date'],
            'service': data['service']
        }
        appointments.append(appointment)
        appointment_id_counter += 1

        return {
            'message': 'Appointment booked successfully.',
            'appointment': appointment
        }, 201

class AppointmentResource(Resource):
    def get(self, id):
        appointment = next((a for a in appointments if a['id'] == id), None)
        if not appointment:
            raise NotFound("Appointment not found.")
        return appointment, 200

    def put(self, id):
        data = request.get_json()
        appointment = next((a for a in appointments if a['id'] == id), None)
        if not appointment:
            raise NotFound("Appointment not found.")

        if 'name' in data:
            appointment['name'] = data['name']
        if 'date' in data:
            if not validate_date_format(data['date']):
                raise BadRequest("Date must be in YYYY-MM-DD format.")
            appointment['date'] = data['date']
        if 'service' in data:
            appointment['service'] = data['service']

        return {
            'message': 'Appointment updated successfully.',
            'appointment': appointment
        }, 200

    def delete(self, id):
        global appointments
        appointment = next((a for a in appointments if a['id'] == id), None)
        if not appointment:
            raise NotFound("Appointment not found.")

        appointments = [a for a in appointments if a['id'] != id]
        return {'message': f'Appointment {id} cancelled successfully.'}, 200

# Register routes
api.add_resource(AppointmentListResource, '/appointments')
api.add_resource(AppointmentResource, '/appointments/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
