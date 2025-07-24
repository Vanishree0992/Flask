from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
api = Api(app)

posts = []
post_id_counter = 1

class PostListResource(Resource):
    def get(self):
        return {'posts': posts}, 200

    def post(self):
        global post_id_counter
        data = request.get_json()

        if not data or 'title' not in data or 'content' not in data:
            raise BadRequest('Title and content are required.')

        new_post = {
            'id': post_id_counter,
            'title': data['title'],
            'content': data['content'],
            'author': data.get('author', 'Anonymous')
        }
        posts.append(new_post)
        post_id_counter += 1
        return new_post, 201

class PostResource(Resource):
    def get(self, id):
        post = next((p for p in posts if p['id'] == id), None)
        if not post:
            raise NotFound('Post not found.')
        return post, 200

    def put(self, id):
        data = request.get_json()
        post = next((p for p in posts if p['id'] == id), None)
        if not post:
            raise NotFound('Post not found.')

        if 'title' in data:
            post['title'] = data['title']
        if 'content' in data:
            post['content'] = data['content']
        if 'author' in data:
            post['author'] = data['author']
        return post, 200

    def delete(self, id):
        global posts
        post = next((p for p in posts if p['id'] == id), None)
        if not post:
            raise NotFound('Post not found.')

        posts = [p for p in posts if p['id'] != id]
        return {'message': f'Post with id {id} deleted.'}, 200

# Register routes
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
