from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    {"text": "Believe in yourself!", "author": "Unknown"},
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Dream big and dare to fail.", "author": "Norman Vaughan"},
    {"text": "What you get by achieving your goals is not as important as what you become by achieving your goals.", "author": "Zig Ziglar"},
    {"text": "Your time is limited, don’t waste it living someone else’s life.", "author": "Steve Jobs"}
]

@app.route('/')
def home():
    initial_quote = random.choice(quotes)
    return render_template('index.html', quote=initial_quote, title="Random Quote Generator")

@app.route('/api/quote')
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)
