from flask import Flask, render_template

app = Flask(__name__)

# Home Page:
@app.route('/')
def home():
    name = "Vanishree"
    profession = "Software Engineer"
    contact = "john.doe@example.com | +1-234-567-890"
    return render_template('home.html', name=name, profession=profession, contact=contact)

# About Page:
@app.route('/about')
def about():
    background = """
    I am a software engineer with 5 years of experience in web development,
    working on Python, Flask, and JavaScript frameworks. I enjoy building
    scalable web applications and solving challenging problems.
    """
    return render_template('about.html', background=background)

# Skills Page:
@app.route('/skills/<name>')
def skills(name):
    skills_dict = {
        'Vani': ['Python', 'Flask', 'JavaScript', 'HTML', 'CSS'],
        'Subha': ['Java', 'Spring', 'Hibernate', 'SQL'],
        'Shree': ['C++', 'Algorithms', 'Data Structures'],
    }
    person_skills = skills_dict.get(name.lower(), ['No skills found.'])
    return render_template('skills.html', name=name, skills=person_skills)

if __name__ == '__main__':
    app.run(debug=True)
