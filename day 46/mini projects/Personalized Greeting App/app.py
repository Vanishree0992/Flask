from flask import Flask

app = Flask(__name__)

# Route: /hello/<name>
@app.route('/hello/<string:name>')
def hello(name):
    return f"""
        <html>
          <body>
            <h1>Hello, {name.title()}!</h1>
            <p>Welcome to the Personalized Greeting App.</p>
          </body>
        </html>
    """

# Route: /greet/<name>/<time>
@app.route('/greet/<string:name>/<string:time>')
def greet(name, time):
    time_lower = time.lower()
    if time_lower == 'morning':
        greeting = f"Good Morning, {name.title()}!"
    elif time_lower == 'evening':
        greeting = f"Good Evening, {name.title()}!"
    else:
        greeting = f"Hello, {name.title()}! Have a great day!"

    return f"""
        <html>
          <body>
            <h1>{greeting}</h1>
          </body>
        </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
