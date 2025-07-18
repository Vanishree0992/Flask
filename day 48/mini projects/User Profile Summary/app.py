from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/profile/<username>")
def profile(username):

    users = {
        "john": {
            "name": "John Doe",
            "bio": "Developer & coffee lover.",
            "joined": datetime.now() - timedelta(days=3),
            "image": "john.jpg"
        },
        "alice": {
            "name": "Alice Smith",
            "bio": "Designer and traveler.",
            "joined": datetime.now() - timedelta(days=10),
            "image": "alice.jpg"
        }
    }

    user = users.get(username)

    if not user:
        return f"User '{username}' not found.", 404

    days_since_joined = (datetime.now() - user["joined"]).days
    is_new = days_since_joined < 7

    return render_template("profile.html", username=username, user=user, is_new=is_new)

if __name__ == "__main__":
    app.run(debug=True)
