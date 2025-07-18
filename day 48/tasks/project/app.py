from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', username="Vanishree", title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404"), 404

if __name__ == '__main__':
    app.run(debug=True)
