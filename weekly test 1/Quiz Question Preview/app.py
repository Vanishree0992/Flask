from flask import Flask, render_template

app = Flask(__name__)

questions = {
    '1': {
        'text': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid']
    },
    '2': {
        'text': 'Which language is used for web apps?',
        'options': ['Python', 'Java', 'C++', 'HTML']
    },
    '3': {
        'text': 'What color is the sky?',
        'options': ['Blue', 'Green', 'Red', 'Yellow']
    }
}

@app.route('/quiz/<question_id>')
def quiz(question_id):
    question = questions.get(question_id)
    if question:
        return render_template('quiz.html', question=question, qid=question_id)
    return "Question not found", 404

if __name__ == '__main__':
    app.run(debug=True)
