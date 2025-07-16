from flask import Flask

app = Flask(__name__)

# Route: /
@app.route('/')
def home():
    return """
    Welcome to the BMI Calculator!<br>
    Usage: /bmi/&lt;weight_kg&gt;/&lt;height_m&gt;<br>
    Example: /bmi/70/1.75
    """

# Route: /bmi/<weight>/<height>
@app.route('/bmi/<float:weight>/<float:height>')
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return f"""
    Your BMI is: {bmi}<br>
    Category: {category}
    """

if __name__ == '__main__':
    app.run(debug=True)


# Flask is lightweight, simple, and flexible — ideal for microservices and single-file tools like this BMI calculator.

# Benefits:

# Minimal boilerplate — just one app.py file to get started.

#  Easy dynamic routes — just add <weight> and <height>.

# Debug mode — see changes instantly.

# Easy to deploy — works locally, or can scale with WSGI servers (Gunicorn, uWSGI)