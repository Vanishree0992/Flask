from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
feedback_list = []

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        feedback_list.append({'name': name, 'message': message})
        return redirect(url_for('thank_you'))
    return render_template('feedback.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html', feedbacks=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)
