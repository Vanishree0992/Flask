from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def color_picker():
    color = "#3498db"  # Default color
    if request.method == 'POST':
        color = request.form.get('color', color)
    return render_template('color.html', selected_color=color)

if __name__ == '__main__':
    app.run(debug=True)
