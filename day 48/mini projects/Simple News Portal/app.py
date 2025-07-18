from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/news')
def news():
    headlines = [
        {
            "title": "New AI Tool Revolutionizes Coding",
            "datetime": datetime(2025, 7, 18, 10, 30),
            "is_breaking": True,
            "category": "technology"
        },
        {
            "title": "Local Elections Announced for August",
            "datetime": datetime(2025, 7, 17, 16, 0),
            "is_breaking": False,
            "category": "politics"
        },
        {
            "title": "Rain Forecast for Southern Region",
            "datetime": datetime(2025, 7, 18, 9, 0),
            "is_breaking": False,
            "category": "weather"
        }
    ]
    return render_template("news.html", headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)
