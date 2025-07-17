from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# 1. /contact – Form with name and message
@app.route('/contact', methods=['GET'])
def contact_form():
    return '''
    <form method="POST" action="/contact">
        Name: <input name="name"><br>
        Message: <textarea name="message"></textarea><br>
        <button type="submit">Send</button>
    </form>
    '''

# 2. request.form['name'] – Get value directly
@app.route('/contact', methods=['POST'])
def contact_submit():
    name = request.form['name']
    message = request.form['message']
    return redirect(f'/thankyou?name={name}&msg={message}')

# 3. /thankyou – After form submit
@app.route('/thankyou')
def thank_you():
    name = request.args.get('name', 'User')
    msg = request.args.get('msg', '')
    return f"Thank you, {name}. We received your message: {msg}"

# 4. Validation – check empty
@app.route('/validate', methods=['GET', 'POST'])
def validate_form():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        if not name or not message:
            return "Both name and message are required!"
        return "Form submitted successfully!"
    return '''
    <form method="POST">
        Name: <input name="name"><br>
        Message: <textarea name="message"></textarea><br>
        <button type="submit">Submit</button>
    </form>
    '''

# 5. Styled HTML output
@app.route('/styled-response', methods=['POST'])
def styled_response():
    name = request.form.get('name')
    msg = request.form.get('message')
    return f'''
    <div style="padding:10px; border:1px solid black;">
        <h2>Response Received</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Message:</strong> {msg}</p>
    </div>
    '''

# 6. request.form.get() – Safe access
@app.route('/safe-form', methods=['POST'])
def safe_form():
    feedback = request.form.get('feedback', 'No feedback provided')
    return f"Feedback: {feedback}"

# 7. Feedback form with rating
@app.route('/rate', methods=['GET', 'POST'])
def rate():
    if request.method == 'POST':
        rating = request.form.get('rating')
        return f"Thanks for rating us: {rating}/5"
    return '''
    <form method="POST">
        Rate us: <select name="rating">
            <option>1</option><option>2</option><option>3</option>
            <option>4</option><option>5</option>
        </select>
        <button type="submit">Submit</button>
    </form>
    '''

# 8. Print form data to terminal
@app.route('/print-form', methods=['POST'])
def print_form():
    data = request.form.to_dict()
    print("Form Data Received:", data)
    return "Form data printed to terminal."

# 9. /register form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        return f"Registered: {name}, Email: {email}"
    return '''
    <form method="POST">
        Name: <input name="name"><br>
        Email: <input name="email"><br>
        Password: <input type="password" name="password"><br>
        <button type="submit">Register</button>
    </form>
    '''

# 10. Show form data as JSON-like dictionary
@app.route('/json-form', methods=['POST'])
def json_form():
    form_data = request.form.to_dict()
    return f"<pre>{form_data}</pre>"
