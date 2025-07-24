from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
api = Api(app)

books = []
book_id_counter = 1

class BookListResource(Resource):
    def get(self):
        author_filter = request.args.get('author')
        if author_filter:
            filtered_books = [b for b in books if b['author'].lower() == author_filter.lower()]
            return {'books': filtered_books}, 200
        return {'books': books}, 200

    def post(self):
        global book_id_counter
        data = request.get_json()
        if not data or 'title' not in data or 'author' not in data or 'year' not in data:
            raise BadRequest("Title, author, and year are required.")

        new_book = {
            'id': book_id_counter,
            'title': data['title'],
            'author': data['author'],
            'year': data['year']
        }
        books.append(new_book)
        book_id_counter += 1
        return new_book, 201

class BookResource(Resource):
    def get(self, id):
        book = next((b for b in books if b['id'] == id), None)
        if not book:
            raise NotFound("Book not found.")
        return book, 200

    def put(self, id):
        data = request.get_json()
        book = next((b for b in books if b['id'] == id), None)
        if not book:
            raise NotFound("Book not found.")

        if 'title' in data:
            book['title'] = data['title']
        if 'author' in data:
            book['author'] = data['author']
        if 'year' in data:
            book['year'] = data['year']
        return book, 200

    def delete(self, id):
        global books
        book = next((b for b in books if b['id'] == id), None)
        if not book:
            raise NotFound("Book not found.")
        books = [b for b in books if b['id'] != id]
        return {'message': f'Book with id {id} deleted.'}, 200

# Routes
api.add_resource(BookListResource, '/books')
api.add_resource(BookResource, '/books/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
