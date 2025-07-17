from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. /method-check – Return current HTTP method
@app.route('/method-check', methods=['GET', 'POST'])
def method_check():
    return f"Method used: {request.method}"

# 2. /submit – Allow only POST, return confirmation
@app.route('/submit', methods=['POST'])
def submit():
    return "POST received. Submission successful."

# 3. /both-methods – Accept both GET and POST
@app.route('/both-methods', methods=['GET', 'POST'])
def both_methods():
    return f"Method used: {request.method}"

# 4. /login – Display a form
@app.route('/login', methods=['GET'])
def login_form():
    return '''
    <form method="POST" action="/login">
      Username: <input name="username">
      <button type="submit">Login</button>
    </form>
    '''

# 5. /login – Handle form POST and show entered username
@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form.get('username')
    return f"Welcome, {username}"

# 6. /admin – Allow only GET
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return "POST not allowed on /admin", 405
    return "Admin panel (GET only)"

# 7. Print method to console
@app.before_request
def log_method():
    print(f"Method: {request.method} on {request.path}")

# 8. /feedback – Display textarea form
@app.route('/feedback', methods=['GET'])
def feedback_form():
    return '''
    <form method="POST" action="/submit-feedback">
      Feedback: <textarea name="feedback"></textarea>
      <button type="submit">Send</button>
    </form>
    '''

# 9. /submit-feedback – Handle POST from feedback
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form.get('feedback')
    return f"Thanks for your feedback: {feedback}"

# 10. /method-form – HTML form supporting GET and POST
@app.route('/method-form', methods=['GET', 'POST'])
def method_form():
    form_html = '''
    <form method="{}">
      Name: <input name="name">
      <button type="submit">Submit</button>
    </form>
    '''
    current_method = request.method
    return render_template_string(form_html.format(current_method.upper())) + f"<p>Current method: {current_method}</p>"
