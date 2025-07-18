from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded movie list by genre
movie_data = {
    "Action": ["Mad Max", "John Wick", "Die Hard"],
    "Comedy": ["Superbad", "The Mask", "Step Brothers"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "Horror": ["The Conjuring", "Get Out", "A Quiet Place"]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    genres = list(movie_data.keys())
    if request.method == 'POST':
        selected_genre = request.form.get('genre')
        return redirect(url_for('show_movies', genre=selected_genre))
    return render_template('index.html', genres=genres)

@app.route('/movies/<genre>')
def show_movies(genre):
    movies = movie_data.get(genre, [])
    return render_template('movies.html', genre=genre, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
