from flask import Flask, render_template

app = Flask(__name__)

@app.route("/testimonials")
def testimonials():
    feedbacks = [
        {
            "name": "Alice",
            "photo": "user.jpg",
            "comment": "Excellent service!",
            "rating": 5
        },
        {
            "name": "Bob",
            "photo": "user.jpg",
            "comment": "Very satisfied with the quality.",
            "rating": 4
        },
        {
            "name": "Charlie",
            "photo": "user.jpg",
            "comment": "Good support, could improve response time.",
            "rating": 3
        }
    ]
    return render_template("testimonials.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
