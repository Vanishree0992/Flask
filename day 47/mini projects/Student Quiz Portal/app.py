from flask import Flask, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'quiz-secret'

# Store scores
quiz_scores = []

# Question/answer key
correct_answers = {
    'q1': 'B',
    'q2': 'A',
    'q3': 'C'
}

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        name = request.form.get('name')
        score = 0

        for q, correct in correct_answers.items():
            if request.form.get(q) == correct:
                score += 1

        # Save result
        quiz_scores.append({'name': name, 'score': score})

        return redirect(url_for('quiz_summary', name=name))
    
    return '''
        <h2>Student Quiz</h2>
        <form method="POST">
            Name: <input name="name" required><br><br>
            1. What is 2 + 2?<br>
            A. 3 <input type="radio" name="q1" value="A"><br>
            B. 4 <input type="radio" name="q1" value="B"><br>
            C. 5 <input type="radio" name="q1" value="C"><br><br>

            2. Capital of France?<br>
            A. Paris <input type="radio" name="q2" value="A"><br>
            B. Rome <input type="radio" name="q2" value="B"><br>
            C. Berlin <input type="radio" name="q2" value="C"><br><br>

            3. HTML stands for?<br>
            A. HighText Machine Language <input type="radio" name="q3" value="A"><br>
            B. Hyper Tool Markup Language <input type="radio" name="q3" value="B"><br>
            C. HyperText Markup Language <input type="radio" name="q3" value="C"><br><br>

            <button type="submit">Submit Quiz</button>
        </form>
    '''

@app.route('/quiz-summary/<name>')
def quiz_summary(name):
    # Find latest score for that name
    entry = next((q for q in reversed(quiz_scores) if q['name'] == name), None)
    if not entry:
        return "<h3>No result found.</h3><a href='/quiz'>Try Quiz</a>"
    return f'''
        <h2>Quiz Summary for {name}</h2>
        <p>Your score: {entry["score"]} / 3</p>
        <a href="/leaderboard">Leaderboard</a>
    '''

@app.route('/leaderboard')
def leaderboard():
    score_filter = request.args.get('score')
    filtered = quiz_scores
    if score_filter:
        try:
            s = int(score_filter)
            filtered = [q for q in quiz_scores if q['score'] == s]
        except:
            return "<h3>Invalid score filter.</h3>"

    if not filtered:
        return "<h3>No entries found.</h3><a href='/quiz'>Take Quiz</a>"

    html = "<h2>Leaderboard</h2><ul>"
    for q in filtered:
        html += f"<li>{q['name']} - {q['score']}</li>"
    html += "</ul><a href='/quiz'>Take Another Quiz</a>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
