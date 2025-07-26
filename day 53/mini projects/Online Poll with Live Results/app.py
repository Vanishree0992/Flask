from flask import Flask, render_template, jsonify, request, session, flash
from flask import redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "secret123"
CORS(app)

# Mock Poll Data
poll_data = {
    "question": "What's your favorite programming language?",
    "options": ["Python", "JavaScript", "C++", "Java"],
    "votes": [0, 0, 0, 0]
}

@app.route('/')
def home():
    message = session.pop('message', None)
    return render_template('index.html', message=message)

@app.route('/api/poll')
def api_poll():
    return jsonify({
        "question": poll_data["question"],
        "options": poll_data["options"],
        "votes": poll_data["votes"]
    })

@app.route('/api/vote', methods=['POST'])
def vote():
    if session.get('voted', False):
        session['message'] = "⚠️ You have already voted!"
        return jsonify({"error": "Already voted"}), 403

    data = request.get_json()
    option_index = data.get("option")

    if option_index is not None and 0 <= option_index < len(poll_data["options"]):
        poll_data["votes"][option_index] += 1
        session['voted'] = True
        return jsonify({"message": "✅ Vote submitted!"})
    return jsonify({"error": "Invalid option"}), 400

if __name__ == '__main__':
    app.run(debug=True)
