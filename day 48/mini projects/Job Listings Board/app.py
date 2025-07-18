from flask import Flask, render_template

app = Flask(__name__)

@app.route('/jobs')
def jobs():
    job_list = [
        {"title": "Backend Developer", "company": "Google", "logo": "google.jpg", "remote": True},
        {"title": "Frontend Developer", "company": "Amazon", "logo": "amazon.jpg", "remote": False},
        {"title": "DevOps Engineer", "company": "Netflix", "logo": "netflix.jpg", "remote": True}
    ]
    return render_template('jobs.html', jobs=job_list)

if __name__ == '__main__':
    app.run(debug=True)
