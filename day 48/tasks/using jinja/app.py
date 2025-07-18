from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    username = "VANISHREE"
    topics = ["Python", "Flask", "Jinja"]
    logged_in = True
    scores = [95, 67, 82, 45, 100]
    current_date = datetime.now()
    tech_skills = {"Python": "Advanced", "Flask": "Intermediate", "SQL": "Beginner"}
    name = "vanishree"
    role = "admin"
    description = "Flask is a lightweight WSGI web application framework for Python."
    
    products = [
        {"title": "Flask Course", "price": "$20", "desc": "Learn Flask from scratch."},
        {"title": "Python Book", "price": "$10", "desc": "A beginner's Python guide."}
    ]

    return render_template(
        'home.html',
        username=username,
        topics=topics,
        logged_in=logged_in,
        scores=scores,
        current_date=current_date,
        tech_skills=tech_skills,
        name=name,
        role=role,
        description=description,
        products=products
    )

if __name__ == '__main__':
    app.run(debug=True)
