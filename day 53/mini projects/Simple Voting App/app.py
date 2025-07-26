from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'secret'

candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

@app.route('/')
def index():
    return render_template("index.html", candidates=candidates)

@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.get_json()
    name = data.get("candidate")
    if name in candidates:
        candidates[name] += 1
        return jsonify({"message": f"Vote recorded for {name}"}), 200
    return jsonify({"error": "Invalid candidate"}), 400

@app.route('/api/results')
def results():
    total_votes = sum(candidates.values())
    return jsonify({
        "results": [
            {"name": name, "votes": votes, "percent": (votes / total_votes * 100) if total_votes else 0}
            for name, votes in candidates.items()
        ],
        "total": total_votes
    })

if __name__ == '__main__':
    app.run(debug=True)
