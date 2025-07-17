from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for certificates
certificates = []

@app.route('/')
@app.route('/quiz-form', methods=['GET'])
def quiz_form():
    return '''
    <h2>Quiz Certificate Form</h2>
    <form method="POST" action="/submit-quiz">
        Name: <input type="text" name="name" required><br><br>
        Score: <input type="number" name="score" required><br><br>
        <button type="submit">Generate Certificate</button>
    </form>
    <br>
    <a href="/certificates?score=10">View Certificates with Score 10</a>
    '''

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    name = request.form.get('name')
    score = request.form.get('score')

    # Store the certificate info
    certificates.append({'name': name, 'score': score})

    # Redirect to certificate page
    return redirect(url_for('show_certificate', name=name, score=score))

@app.route('/certificate/<name>/<score>')
def show_certificate(name, score):
    return f'''
    <h2>🎉 Certificate of Achievement</h2>
    <p>This is to certify that <strong>{name}</strong> has successfully completed the quiz with a score of <strong>{score}</strong>.</p>
    <a href="/">Back to Form</a>
    '''

@app.route('/certificates')
def filter_certificates():
    score_filter = request.args.get('score')
    filtered = [c for c in certificates if c['score'] == score_filter] if score_filter else certificates

    if not filtered:
        return "<p>No certificates found for that score.</p>"

    links = ''.join(
        f"<li><a href='{url_for('show_certificate', name=c['name'], score=c['score'])}'>{c['name']} - Score: {c['score']}</a></li>"
        for c in filtered
    )
    return f"<h3>Certificates with score {score_filter}:</h3><ul>{links}</ul>"

if __name__ == '__main__':
    app.run(debug=True)
