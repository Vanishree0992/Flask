from flask import Flask, request, redirect, url_for

app = Flask(__name__)

feedback_store = []

# 1. /feedback-form: Show form to collect name, email, message
@app.route('/feedback-form', methods=['GET'])
def feedback_form():
    return '''
    <h2>Customer Feedback Form</h2>
    <form method="POST" action="/submit-feedback">
        Name: <input type="text" name="name"><br>
        Email: <input type="email" name="email"><br>
        Message:<br><textarea name="message"></textarea><br>
        <button type="submit">Submit</button>
    </form>
    '''

# 2. /submit-feedback: Handle POST and redirect to /thank-you
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    feedback_store.append({'name': name, 'email': email, 'message': message})
    return redirect(url_for('thank_you', user=name))

# 3. /thank-you: Thank user
@app.route('/thank-you')
def thank_you():
    user = request.args.get('user', 'Guest')
    return f"<h2>Thank You, {user}!</h2><p>Your feedback has been received.</p>"

# 4. /feedbacks?user=name: Filtered feedback by name
@app.route('/feedbacks')
def view_feedbacks():
    user = request.args.get('user')
    if not user:
        return "<h3>No user specified. Add ?user=Name in the URL.</h3>"

    user_feedbacks = [fb for fb in feedback_store if fb['name'].lower() == user.lower()]
    
    if not user_feedbacks:
        return f"<h3>No feedback found for {user}</h3>"

    response = f"<h2>Feedback from {user}:</h2><ul>"
    for fb in user_feedbacks:
        response += f"<li><strong>Email:</strong> {fb['email']}<br><strong>Message:</strong> {fb['message']}</li><br>"
    response += "</ul>"
    return response

# 5. /user/<username>: Dynamic route for user-specific data
@app.route('/user/<username>')
def user_profile(username):
       return f"<h2>Welcome, {username}!</h2><p>This is your feedback dashboard.</p>"
