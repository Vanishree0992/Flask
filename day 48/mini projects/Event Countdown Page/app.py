from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/event")
def event():
    event_name = "Hackathon 2025"
    event_datetime = datetime(2025, 8, 1, 10, 0, 0)  # Example event date and time

    now = datetime.now()
    event_started = now >= event_datetime

    return render_template(
        "event.html",
        event_name=event_name,
        event_datetime=event_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
        event_started=event_started
    )

if __name__ == "__main__":
    app.run(debug=True)
