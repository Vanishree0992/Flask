from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 1. Send name to template using dynamic route
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, title="User Page")

# 2. Pass list of courses
@app.route('/courses')
def courses():
    course_list = ['Python', 'Flask', 'HTML', 'CSS']
    return render_template('courses.html', courses=course_list, title="Courses")

# 3. Boolean flag for login/logout
@app.route('/profile')
def profile():
    is_logged_in = True
    user_info = {'name': 'Mahesh', 'email': 'mahesh@example.com'}
    return render_template('profile.html', is_logged_in=is_logged_in, user=user_info, title="Profile")

# 4 & 5. Dictionary + current date/time
@app.route('/user-details')
def user_details():
    user_profile = {
        'name': 'Vanishree',
        'age': 25,
        'city': 'Chennai'
    }
    now = datetime.now()
    return render_template('profile.html', user=user_profile, current_time=now, title="User Details", is_logged_in=True)

# 6. News list
@app.route('/news')
def news():
    news_items = ["Exam starts next week", "New courses available", "Server maintenance on Sunday"]
    return render_template('news.html', news_items=news_items, title="News")

# 7. Profile card
@app.route('/card')
def card():
    return render_template('profile.html', name="Amit", age=28, city="Delhi", title="Profile Card", is_logged_in=True)

# 8 & 9. Products list
@app.route('/products')
def products():
    product_list = [
        {"name": "Pen", "price": 10},
        {"name": "Notebook", "price": 50},
        {"name": "Bag", "price": 500}
    ]
    return render_template('product_list.html', products=product_list, title="Products")

# 10. Tax calculation
@app.route('/tax')
def tax():
    price = 1000
    tax_rate = 0.18
    tax = price * tax_rate
    total = price + tax
    return render_template("product_list.html", price=price, tax=tax, total=total, title="Tax Details")

if __name__ == '__main__':
    app.run(debug=True)
