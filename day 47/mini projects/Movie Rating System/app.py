from flask import Flask, request, redirect, url_for

app = Flask(__name__)

ratings = []

@app.route('/')
@app.route('/rate', methods=['GET'])
def rate_form():
    return '''
    <h2>🎬 Movie Rating Form</h2>
    <form method="POST" action="/submit-rating">
        Your Name: <input type="text" name="name" required><br><br>
        Movie Title: <input type="text" name="movie" required><br><br>
        Rating (1-5): <input type="number" name="rating" min="1" max="5" required><br><br>
        <button type="submit">Submit Rating</button>
    </form>
    <br>
    <a href="/ratings?movie=Inception">View Ratings for Inception</a>
    '''

@app.route('/submit-rating', methods=['POST'])
def submit_rating():
    name = request.form['name']
    movie = request.form['movie']
    rating = request.form['rating']
    
    ratings.append({'name': name, 'movie': movie, 'rating': rating})
    return redirect(url_for('thank_you', name=name))

@app.route('/thank-you/<name>')
def thank_you(name):
    return f"<h3>Thank you, {name}, for your rating!</h3><a href='/rate'>Rate Another</a>"

@app.route('/ratings')
def show_ratings():
    movie_filter = request.args.get('movie')
    filtered = [r for r in ratings if r['movie'].lower() == movie_filter.lower()] if movie_filter else ratings

    if not filtered:
        return f"<h3>No ratings found for '{movie_filter}'</h3><a href='/rate'>Back</a>"

    output = f"<h3>Ratings for '{movie_filter}':</h3><ul>"
    for r in filtered:
        output += f"<li>{r['name']} rated it {r['rating']} stars</li>"
    output += "</ul><a href='/rate'>Back</a>"
    return output

@app.route('/movie/<title>')
def movie_info(title):
    return f"<h3>Movie Info: {title.title()}</h3><p>This is placeholder info for {title.title()}.</p><a href='/rate'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
