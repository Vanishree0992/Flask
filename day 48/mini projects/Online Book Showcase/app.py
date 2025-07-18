from flask import Flask, render_template

app = Flask(__name__)

books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "image": "book1.jpg"},
    {"title": "Atomic Habits", "author": "James Clear", "image": "book2.jpg"},
    {"title": "1984", "author": "George Orwell", "image": "book3.jpg"}
]

@app.route('/books')
def show_books():
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
