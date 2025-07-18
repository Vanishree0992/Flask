from flask import Flask, render_template

app = Flask(__name__)

@app.route('/movies')
def movies():
    movie_list = [
        {"title": "Inception", "poster": "inception.jpg", "rating": 5, "new": False},
        {"title": "Oppenheimer", "poster": "oppenheimer.jpg", "rating": 4, "new": True},
        {"title": "Dune", "poster": "dune.jpg", "rating": 5, "new": True}
    ]
    return render_template("movies.html", movies=movie_list)

if __name__ == '__main__':
    app.run(debug=True)
