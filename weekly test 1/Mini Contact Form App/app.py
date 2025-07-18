from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

submitted_data = {}

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        submitted_data[name] = {'email': email, 'message': message}
        return redirect(url_for('thank_you', name=name))
    return render_template('contact.html')

@app.route('/thankyou/<name>')
def thank_you(name):
    data = submitted_data.get(name)
    if not data:
        return "No submission found for this name.", 404
    return render_template('thankyou.html', name=name, email=data['email'], message=data['message'])

if __name__ == '__main__':
    app.run(debug=True)
