from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    time = request.args.get('time', 'day')
    return f"<h2>Good {time}, {name}!</h2>"

@app.route('/custom-greet/<name>')
def custom_greet(name):
    return f"<h2>Hello, {name}! This is your custom greeting 🎉</h2>"

@app.route('/submit-greet', methods=['POST'])
def submit_greet():
    name = request.form.get('name')
    time = request.form.get('time')
    return redirect(url_for('greet', name=name, time=time))

@app.route('/greet-result')
def greet_result():
    name = request.args.get('name', 'Guest')
    return f"<h3>Thank you {name} for using the greeting service!</h3>"

@app.route('/')
def home():
    return '''
    <h2>Custom Greeting Generator</h2>
    <form method="POST" action="/submit-greet">
        Name: <input name="name" required><br><br>
        Time of Day:
        <select name="time">
            <option value="morning">Morning</option>
            <option value="afternoon">Afternoon</option>
            <option value="evening">Evening</option>
            <option value="night">Night</option>
        </select><br><br>
        <button type="submit">Generate Greeting</button>
    </form>
    <br>
    Try: <a href="/greet?name=Arivu&time=morning">/greet?name=Arivu&time=morning</a><br>
    Try: <a href="/custom-greet/Arivu">/custom-greet/Arivu</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
