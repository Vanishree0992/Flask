from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/greet')
def greet():
    hour = request.args.get('hour', default=9, type=int)

    if 5 <= hour <= 11:
        greeting = "Good Morning"
    elif 12 <= hour <= 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Night"

    return render_template("greet.html", hour=hour, greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)

