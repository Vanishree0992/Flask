from flask import Flask, render_template

app = Flask(__name__)

@app.route('/blogs')
def blogs():
    blog_list = [
        {"title": "Why Flask is Great", "author": "Alice", "snippet": "Flask is a lightweight WSGI web application framework...", "featured": True, "image": "featured.jpg"},
        {"title": "Understanding REST APIs", "author": "Bob", "snippet": "REST APIs allow seamless data exchange...", "featured": False, "image": "regular.jpg"},
        {"title": "Python Tips & Tricks", "author": "Carol", "snippet": "Boost your productivity with these simple tips...", "featured": False, "image": "regular.jpg"}
    ]
    return render_template("blogs.html", blogs=blog_list)

if __name__ == '__main__':
    app.run(debug=True)
