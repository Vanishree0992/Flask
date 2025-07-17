from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Simulated mood log data
mood_entries = []

@app.route('/log-mood', methods=['GET', 'POST'])
def log_mood():
    if request.method == 'POST':
        name = request.form.get('name')
        mood = request.form.get('mood')
        reason = request.form.get('reason')
        
        # Save entry
        mood_entries.append({'name': name, 'mood': mood, 'reason': reason})
        
        # Redirect to thank-you
        return redirect(url_for('thank_you', name=name))
    
    return '''
        <h2>Log Your Mood</h2>
        <form method="POST">
            Name: <input name="name" required><br><br>
            Mood: <input name="mood" required><br><br>
            Reason: <input name="reason"><br><br>
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/thank-you/<name>')
def thank_you(name):
    return f'''
        <h3>Thank you, {name}!</h3>
        <p>Your mood has been recorded.</p>
        <a href="/logs">View All Logs</a>
    '''

@app.route('/logs')
def view_logs():
    filter_mood = request.args.get('mood')
    filtered = mood_entries if not filter_mood else [entry for entry in mood_entries if entry['mood'].lower() == filter_mood.lower()]
    
    if not filtered:
        return "<h3>No mood logs found.</h3><a href='/log-mood'>Back</a>"
    
    html = "<h2>Mood Logs</h2><ul>"
    for entry in filtered:
        html += f"<li><strong>{entry['name']}</strong>: {entry['mood']} – {entry['reason']}</li>"
    html += "</ul><a href='/log-mood'>Log Another Mood</a>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
