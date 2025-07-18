from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
user_profiles = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create-profile', methods=['POST'])
def create_profile():
    name = request.form['name']
    skills = request.form['skills']
    bio = request.form['bio']
    
    user_profiles[name] = {
        'skills': skills.split(','),
        'bio': bio
    }
    
    return redirect(url_for('profile', name=name))

@app.route('/profile/<name>')
def profile(name):
    profile_data = user_profiles.get(name)
    if profile_data:
        return render_template('profile.html', name=name, skills=profile_data['skills'], bio=profile_data['bio'])
    return "Profile not found", 404

if __name__ == '__main__':
    app.run(debug=True)
