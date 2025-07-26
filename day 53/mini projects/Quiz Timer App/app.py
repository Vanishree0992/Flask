from flask import Flask, render_template, jsonify, session
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'secret123'

QUIZ_DURATION = 60  # seconds

quiz_questions = [
    {"id": 1, "question": "What is 2 + 2?"},
    {"id": 2, "question": "What is the capital of India?"},
    {"id": 3, "question": "What is the color of the sky?"}
]

@app.route('/')
def quiz():
    if 'quiz_end' not in session:
        session['quiz_end'] = (datetime.utcnow() + timedelta(seconds=QUIZ_DURATION)).isoformat()
    return render_template("quiz.html", questions=quiz_questions, title="Timed Quiz")

@app.route('/api/timer')
def timer():
    end_time = datetime.fromisoformat(session.get('quiz_end'))
    now = datetime.utcnow()
    remaining = max(0, int((end_time - now).total_seconds()))
    return jsonify({"remaining": remaining})

if __name__ == '__main__':
    app.run(debug=True)
