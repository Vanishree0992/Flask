from flask import Flask, render_template

app = Flask(__name__)

@app.route("/faq")
def faq():
    faqs = [
        {"question": "What is your return policy?", "answer": "You can return items within 30 days."},
        {"question": "How do I track my order?", "answer": "Use the tracking link in your confirmation email."},
        {"question": "Can I change my shipping address?", "answer": None},  # Unanswered
    ]
    return render_template("faq.html", faqs=faqs)

if __name__ == "__main__":
    app.run(debug=True)
