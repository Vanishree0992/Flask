from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

news_data = {
    "tech": [
        {"title": "AI Beats Humans at Chess Again", "content": "A new AI system has defeated the world champion..."},
        {"title": "Quantum Computing Breakthrough", "content": "Scientists achieve new milestone in quantum computing..."},
    ],
    "sports": [
        {"title": "India Wins Cricket Series", "content": "India defeats Australia in thrilling finale..."},
        {"title": "Olympics 2024 Preview", "content": "Athletes gear up for Paris Olympics with intense training..."},
    ],
    "world": [
        {"title": "Global Summit on Climate", "content": "Leaders gather to discuss environmental strategies..."},
        {"title": "New Trade Agreements Signed", "content": "Nations agree to reduce tariffs for sustainable growth..."},
    ]
}

@app.route('/')
def index():
    default_category = "tech"
    return render_template("index.html", category=default_category, title="News Feed Reader")

@app.route('/api/news')
def get_news():
    # Simulate random category each fetch (or can use request.args.get('category'))
    category = random.choice(list(news_data.keys()))
    return jsonify({"category": category, "articles": news_data[category]})

if __name__ == '__main__':
    app.run(debug=True)
