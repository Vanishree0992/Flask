from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {"title": "Portfolio Website", "description": "A personal portfolio using Flask."},
    {"title": "E-Commerce Site", "description": "Online store with cart and checkout."},
    {"title": "Blog System", "description": "A simple blog with login and CRUD."}
]

@app.route('/')
def home():
    return render_template("home.html", name="Vanishree", available=True)

@app.route('/about')
def about():
    skills = ["Python", "Flask", "HTML", "CSS", "JavaScript"]
    return render_template("about.html", skills=skills)

@app.route('/projects')
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
