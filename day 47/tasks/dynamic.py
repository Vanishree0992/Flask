from flask import Flask, request

app = Flask(__name__)

# 1. /hello/<name>
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

# 2. /square/<int:number>
@app.route('/square/<int:number>')
def square(number):
    return f"Square of {number} is {number ** 2}"

# 3. /greet/<name>/<int:age>
@app.route('/greet/<name>/<int:age>')
def greet(name, age):
    return f"Hi {name}, you are {age} years old."

# 4. /status/<username>/<status>
@app.route('/status/<username>/<status>')
def status(username, status):
    return f"User {username} is now {status}."

# 5. /price/<float:amount>
@app.route('/price/<float:amount>')
def price(amount):
    return f"The price is ${amount:.2f}"

# 6. /profile/<username>
@app.route('/profile/<username>')
def profile(username):
    return f"""
    <html>
      <body>
        <h2>User Profile</h2>
        <p>Username: {username}</p>
      </body>
    </html>
    """

# 7. /math/<int:x>/<int:y>
@app.route('/math/<int:x>/<int:y>')
def math(x, y):
    return f"Sum = {x + y}, Difference = {x - y}, Product = {x * y}"

# 8. /file/<path:filename>
@app.route('/file/<path:filename>')
def file(filename):
    return f"Requested file: {filename}"

# 9. /color/<string:color>
@app.route('/color/<string:color>')
def color(color):
    return f"<h2 style='color:{color}'>This text is in {color}.</h2>"

# 10. /language/<lang>
@app.route('/language/<lang>')
def language(lang):
    supported = ['python', 'java', 'c++']
    return f"{lang} is supported." if lang.lower() in supported else "Language not supported."

# 11. /user/<username> – validate username
@app.route('/user/<username>')
def user(username):
    allowed = ['admin', 'trainer', 'student']
    return f"Welcome, {username}!" if username in allowed else "User not found."

# 12. /country/<code>
@app.route('/country/<code>')
def country(code):
    countries = {'IN': 'India', 'US': 'United States', 'UK': 'United Kingdom'}
    return countries.get(code.upper(), 'Country not found')

# 13. /debug/<info>
@app.route('/debug/<info>')
def debug(info):
    print("Debugging info:", info)
    return f"Debug: {info}"

# 14. /html/<name>/<int:age> with triple quotes
@app.route('/html/<name>/<int:age>')
def html_output(name, age):
    return f"""
    <html>
      <body>
        <h1>User Info</h1>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
      </body>
    </html>
    """

# 15. /error/<int:code>
@app.route('/error/<int:code>')
def error(code):
    errors = {
        404: "Error 404: Page Not Found",
        500: "Error 500: Internal Server Error",
        403: "Error 403: Forbidden"
    }
    return errors.get(code, "Unknown Error Code")
