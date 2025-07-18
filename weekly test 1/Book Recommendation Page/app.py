from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample genre-based book data
book_data = {
    'fiction': ['The Great Gatsby', 'To Kill a Mockingbird', '1984'],
    'mystery': ['Gone Girl', 'The Girl with the Dragon Tattoo', 'Sherlock Holmes'],
    'sci-fi': ['Dune', 'Ender\'s Game', 'The Martian'],
    'fantasy': ['Harry Potter', 'The Hobbit', 'Mistborn'],
    'nonfiction': ['Sapiens', 'Educated', 'Atomic Habits']
}

@app.route('/', methods=['GET', 'POST'])
def genre_form():
    if request.method == 'POST':
        genre = request.form['genre'].lower()
        return redirect(url_for('recommendations', genre=genre))
    return render_template('genre_form.html')

@app.route('/books/<genre>')
def recommendations(genre):
    books = book_data.get(genre, [])
    return render_template('recommendations.html', genre=genre.title(), books=books)

if __name__ == '__main__':
    app.run(debug=True)
