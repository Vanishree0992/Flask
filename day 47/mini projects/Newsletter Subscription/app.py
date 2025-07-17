from flask import Flask, request, redirect, url_for

app = Flask(__name__)

subscribers = []

@app.route('/')
@app.route('/subscribe', methods=['GET'])
def subscribe_form():
    return '''
    <h2>📰 Newsletter Subscription</h2>
    <form method="POST" action="/submit-subscription">
        Name: <input type="text" name="name" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        Month: <input type="text" name="month" placeholder="e.g., July" required><br><br>
        <button type="submit">Subscribe</button>
    </form>
    <br>
    <a href="/subscribers?month=July">View July Subscribers</a>
    '''

@app.route('/submit-subscription', methods=['POST'])
def submit_subscription():
    name = request.form.get('name')
    email = request.form.get('email')
    month = request.form.get('month')

    subscribers.append({'name': name, 'email': email, 'month': month})

    return redirect(url_for('thank_you', name=name))

@app.route('/thanks/<name>')
def thank_you(name):
    return f'''
    <h3>🎉 Thank you, {name}!</h3>
    <p>You’ve successfully subscribed to our newsletter.</p>
    <a href="/">Back to Home</a>
    '''

@app.route('/subscribers')
def list_subscribers():
    month_filter = request.args.get('month')
    filtered = [s for s in subscribers if s['month'].lower() == month_filter.lower()] if month_filter else subscribers

    if not filtered:
        return f"<p>No subscribers found for {month_filter}.</p>"

    items = ''.join(f"<li>{s['name']} ({s['email']}) - {s['month']}</li>" for s in filtered)
    return f"<h3>Subscribers for {month_filter}:</h3><ul>{items}</ul>"

if __name__ == '__main__':
    app.run(debug=True)
