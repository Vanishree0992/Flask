from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/achievements")
def achievements():
    current_year = datetime.now().year
    data = {
        "2025": ["Won National Hackathon", "Expanded to 3 new countries"],
        "2024": ["Launched new product line", "Secured Series B funding"],
        "2023": ["Reached 1M users", "Opened new HQ"],
    }
    return render_template("achievements.html", data=data, current_year=str(current_year))

if __name__ == "__main__":
    app.run(debug=True)
