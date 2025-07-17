from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory donation list
donations = []

@app.route('/')
def home():
    return '''
    <h2>Online Donation</h2>
    <form method="POST" action="/donate-confirm">
        Name: <input name="name" required><br><br>
        Amount: <input type="number" name="amount" required><br><br>
        Purpose:
        <select name="purpose">
            <option value="education">Education</option>
            <option value="healthcare">Healthcare</option>
            <option value="environment">Environment</option>
        </select><br><br>
        <button type="submit">Donate</button>
    </form>
    <br>
    <a href="/donations?purpose=education">View Education Donations</a>
    '''

@app.route('/donate-confirm', methods=['POST'])
def confirm_donation():
    name = request.form.get('name')
    amount = request.form.get('amount')
    purpose = request.form.get('purpose')

    # Store in memory
    donations.append({'name': name, 'amount': amount, 'purpose': purpose})

    return redirect(url_for('thank_donor', name=name))

@app.route('/thank-donor/<name>')
def thank_donor(name):
    return f"<h2>Thank You, {name}!</h2><p>Your donation has been received.</p>"

@app.route('/donations')
def filter_donations():
    purpose = request.args.get('purpose')
    filtered = [d for d in donations if d['purpose'] == purpose] if purpose else donations

    if not filtered:
        return "<p>No donations found for this purpose.</p>"

    donation_list = ''.join(
        f"<li>{d['name']} donated ₹{d['amount']} for {d['purpose'].title()}</li>"
        for d in filtered
    )
    return f"<h3>Donations for {purpose.title() if purpose else 'All'}:</h3><ul>{donation_list}</ul>"

if __name__ == '__main__':
    app.run(debug=True)
