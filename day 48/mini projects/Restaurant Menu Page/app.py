from flask import Flask, render_template

app = Flask(__name__)

@app.route('/menu')
def menu():
    menu_data = {
        "Starters": [
            {"name": "Caesar Salad", "image": "salad.jpg", "available": True},
            {"name": "Garlic Bread", "image": "salad.jpg", "available": False}
        ],
        "Main Course": [
            {"name": "Grilled Steak", "image": "steak.jpg", "available": True},
            {"name": "Veg Lasagna", "image": "steak.jpg", "available": True}
        ],
        "Desserts": [
            {"name": "Ice Cream", "image": "icecream.jpg", "available": False},
            {"name": "Brownie", "image": "icecream.jpg", "available": True}
        ]
    }
    return render_template('menu.html', menu=menu_data)

if __name__ == '__main__':
    app.run(debug=True)
