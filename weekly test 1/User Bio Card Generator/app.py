from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        hobbies = request.form['hobbies'].split(',')
        hobbies = [hobby.strip() for hobby in hobbies if hobby.strip()]
        return render_template('bio_card.html', name=name, age=age, hobbies=hobbies)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
