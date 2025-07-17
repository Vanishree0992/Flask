from flask import Flask, redirect, url_for, request

app = Flask(__name__)

# 1. /start – Redirect to /home
@app.route('/start')
def start():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return "Welcome to the Home Page!"

# 2. /dashboard – Redirect to /login if not logged in (simulate)
@app.route('/dashboard')
def dashboard():
    logged_in = request.args.get('logged_in')  # Simulate login
    if logged_in != 'true':
        return redirect(url_for('login_form'))
    return "Welcome to your Dashboard!"

# Reuse login form from previous section
@app.route('/login', methods=['GET'])
def login_form():
    return '''
    <form method="POST" action="/login">
        Username: <input name="username">
        <button type="submit">Login</button>
    </form>
    '''

@app.route('/login', methods=['POST'])
def login_process():
    username = request.form.get('username')
    return f"Logged in as {username}"

# 3. Generate profile link using url_for()
@app.route('/link-builder')
def link_builder():
    link = url_for('user_profile', username='mahesh')
    return f'<a href="{link}">Go to Mahesh’s Profile</a>'

@app.route('/profile/<username>')
def user_profile(username):
    return f"User Profile Page: {username}"

# 4. HTML page with multiple url_for() links
@app.route('/menu')
def menu():
    home_link = url_for('home')
    login_link = url_for('login_form')
    profile_link = url_for('user_profile', username='guest')
    return f'''
    <ul>
        <li><a href="{home_link}">Home</a></li>
        <li><a href="{login_link}">Login</a></li>
        <li><a href="{profile_link}">Guest Profile</a></li>
    </ul>
    '''

# 5. Redirect after any form to /thankyou
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        return redirect(url_for('thankyou_page'))
    return '''
    <form method="POST">
        <input name="data">
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/thankyou')
def thankyou_page():
    return "Thank you for submitting the form!"
