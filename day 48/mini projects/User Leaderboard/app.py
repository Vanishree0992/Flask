from flask import Flask, render_template

app = Flask(__name__)

@app.route("/leaderboard")
def leaderboard():
    leaderboard_data = [
        {"name": "Alice", "score": 980},
        {"name": "Bob", "score": 920},
        {"name": "Charlie", "score": 890},
        {"name": "Diana", "score": 850},
    ]
    return render_template("leaderboard.html", leaderboard=leaderboard_data)

if __name__ == "__main__":
    app.run(debug=True)
