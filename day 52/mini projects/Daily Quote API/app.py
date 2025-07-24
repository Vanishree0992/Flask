from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest, NotFound
import random

app = Flask(__name__)
api = Api(app)

quotes = []
quote_id_counter = 1

class QuoteListResource(Resource):
    def get(self):
        return {'quotes': quotes}, 200

    def post(self):
        global quote_id_counter
        data = request.get_json()

        if not data or 'text' not in data:
            raise BadRequest("Quote 'text' is required.")

        new_quote = {
            'id': quote_id_counter,
            'text': data['text']
        }
        quotes.append(new_quote)
        quote_id_counter += 1
        return new_quote, 201

class QuoteResource(Resource):
    def get(self, id):
        quote = next((q for q in quotes if q['id'] == id), None)
        if not quote:
            raise NotFound("Quote not found.")
        return quote, 200

    def put(self, id):
        data = request.get_json()
        quote = next((q for q in quotes if q['id'] == id), None)
        if not quote:
            raise NotFound("Quote not found.")

        if 'text' in data:
            quote['text'] = data['text']
        return quote, 200

    def delete(self, id):
        global quotes
        quote = next((q for q in quotes if q['id'] == id), None)
        if not quote:
            raise NotFound("Quote not found.")
        quotes = [q for q in quotes if q['id'] != id]
        return {'message': f'Quote with id {id} deleted.'}, 200

class RandomQuoteResource(Resource):
    def get(self):
        if not quotes:
            return {'message': 'No quotes available yet. Please add some first!'}, 404
        return random.choice(quotes), 200

# Route definitions
api.add_resource(QuoteListResource, '/quotes')
api.add_resource(QuoteResource, '/quotes/<int:id>')
api.add_resource(RandomQuoteResource, '/quote/random')

if __name__ == '__main__':
    app.run(debug=True)
