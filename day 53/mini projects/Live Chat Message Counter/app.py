from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def chat():
    return render_template("chat.html", title="Live Chat Message Counter")

@app.route('/api/messages/count')
def message_count():
    # Simulate live count (replace with real logic if needed)
    count = random.randint(100, 999)
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run(debug=True)
