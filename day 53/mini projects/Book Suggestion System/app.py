from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "summary": "A journey of self-discovery and following one’s dreams."},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "summary": "A classic novel on racial injustice and human empathy."},
    {"title": "1984", "author": "George Orwell", "summary": "A dystopian future under totalitarian rule."},
    {"title": "Atomic Habits", "author": "James Clear", "summary": "A powerful guide on building good habits and breaking bad ones."},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "summary": "A romantic novel exploring manners, upbringing, and love."}
]

@app.route('/')
def home():
    return render_template("index.html", title="Book Suggestion")

@app.route('/api/book/suggest')
def suggest_book():
    return jsonify(random.choice(books))

if __name__ == '__main__':
    app.run(debug=True)
