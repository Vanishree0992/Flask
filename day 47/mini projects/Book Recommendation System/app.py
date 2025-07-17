from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Sample book data
book_data = {
    'sci-fi': ['Dune', 'Neuromancer', 'Foundation'],
    'romance': ['Pride and Prejudice', 'Me Before You', 'The Notebook']
}

@app.route('/')
def home():
    return '''
    <h2>Book Recommendation Form</h2>
    <form method="POST" action="/show-recommendation">
        Name: <input name="user" required><br><br>
        Genre:
        <select name="genre">
            <option value="sci-fi">Sci-Fi</option>
            <option value="romance">Romance</option>
        </select><br><br>
        <button type="submit">Get Recommendations</button>
    </form>
    <br>
    Try filtering: <a href="/books?genre=sci-fi">/books?genre=sci-fi</a><br>
    Try book detail: <a href="/book/Dune">/book/Dune</a>
    '''

@app.route('/show-recommendation', methods=['POST'])
def show_recommendation():
    user = request.form.get('user')
    genre = request.form.get('genre')
    return redirect(url_for('thanks', user=user, genre=genre))

@app.route('/thanks/<user>')
def thanks(user):
    genre = request.args.get('genre', '')
    recommendations = book_data.get(genre, [])
    book_list = '<ul>' + ''.join(f'<li>{book}</li>' for book in recommendations) + '</ul>'
    return f'''
    <h2>Thank you, {user}!</h2>
    <p>Recommended {genre.title()} Books:</p>
    {book_list}
    '''

@app.route('/books')
def books_by_genre():
    genre = request.args.get('genre')
    if genre in book_data:
        books = book_data[genre]
        return f"<h3>Books in {genre.title()}:</h3><ul>" + ''.join(f"<li>{b}</li>" for b in books) + "</ul>"
    return "<p>No genre selected or genre not found.</p>"

@app.route('/book/<title>')
def book_detail(title):
    return f"<h3>Book Detail Page</h3><p>You selected: <strong>{title}</strong></p>"

if __name__ == '__main__':
    app.run(debug=True)
