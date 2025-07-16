from flask import Flask

app = Flask(__name__)

# Route: /user/<name>
@app.route('/user/<string:name>')
def user(name):
    print(f"[LOG] /user accessed with name: {name}")  # Console log
    return f"<h1>Welcome, {name.title()}!</h1>"

# Route: /user/<name>/location/<city>
@app.route('/user/<string:name>/location/<string:city>')
def user_location(name, city):
    print(f"[LOG] /user/{name}/location/{city} accessed")  # Console log
    return f"<h1>Hi {name.title()}, how is {city.title()}?</h1>"

if __name__ == '__main__':
    app.run(debug=True)
