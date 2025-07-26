from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

notifications = [
    {"id": 1, "message": "New assignment uploaded."},
    {"id": 2, "message": "Your profile was viewed."},
    {"id": 3, "message": "Meeting scheduled for 3 PM."}
]

@app.route('/')
def index():
    return render_template("index.html", title="Simple Notification Bell")

@app.route('/api/notifications')
def get_notifications():
    unread = random.sample(notifications, random.randint(0, len(notifications)))
    return jsonify({"unread_count": len(unread), "messages": unread})

if __name__ == '__main__':
    app.run(debug=True)
