from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/gallery")
def gallery():
    image_folder = os.path.join(app.static_folder, "images/gallery")
    images = os.listdir(image_folder)
    image_paths = [f"images/gallery/{img}" for img in images if img.endswith((".jpg", ".png", ".jpeg"))]
    return render_template("gallery.html", photos=image_paths)

if __name__ == "__main__":
    app.run(debug=True)
