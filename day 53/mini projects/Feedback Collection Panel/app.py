from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
feedback_list = []  # In-memory storage

@app.route('/')
def index():
    return render_template('index.html', title="Feedback Collection Panel")

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({"error": "Name and message are required."}), 400

    feedback_list.append({"name": name, "message": message})
    return jsonify({"message": "Thank you for your feedback!"}), 200

@app.route('/api/feedbacks')
def get_feedbacks():
    return jsonify(feedback_list)

if __name__ == '__main__':
    app.run(debug=True)
