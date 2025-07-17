from flask import Flask, request, redirect, url_for

app = Flask(__name__)

complaints = []

@app.route('/')
def home():
    return '''
    <h2>Customer Complaint Portal</h2>
    <form method="POST" action="/complaint-submit">
        Name: <input type="text" name="name" required><br><br>
        Issue: <textarea name="issue" required></textarea><br><br>
        Urgency:
        <select name="urgency">
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
        </select><br><br>
        <button type="submit">Submit Complaint</button>
    </form>
    <br>
    <a href="/complaints?urgency=high">View High Urgency Complaints</a>
    '''

@app.route('/complaint-submit', methods=['POST'])
def complaint_submit():
    name = request.form.get('name')
    issue = request.form.get('issue')
    urgency = request.form.get('urgency')

    complaints.append({'name': name, 'issue': issue, 'urgency': urgency})
    return redirect(url_for('complaint_status', name=name))

@app.route('/complaint-status/<name>')
def complaint_status(name):
    return f"<h3>Thank you, {name}. Your complaint has been submitted.</h3>"

@app.route('/complaints')
def view_complaints():
    urgency = request.args.get('urgency')
    filtered = [c for c in complaints if c['urgency'] == urgency] if urgency else complaints

    if not filtered:
        return "<p>No complaints found.</p>"

    complaint_list = ''.join(
        f"<li>{c['name']} - {c['issue']} ({c['urgency'].capitalize()})</li>" for c in filtered
    )
    return f"<h3>Complaints ({urgency.capitalize() if urgency else 'All'}):</h3><ul>{complaint_list}</ul>"

if __name__ == '__main__':
    app.run(debug=True)
