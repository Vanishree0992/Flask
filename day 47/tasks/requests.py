from flask import Flask, request

app = Flask(__name__)

# 1. /search?keyword=flask
@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    return f"Search keyword: {keyword}" if keyword else "No keyword found."

# 2. /filter?type=shirt&color=blue&size=m
@app.route('/filter')
def filter_items():
    item_type = request.args.get('type')
    color = request.args.get('color')
    size = request.args.get('size')
    return f"Filter - Type: {item_type}, Color: {color}, Size: {size}"

# 3. Handle missing keyword
@app.route('/safe-search')
def safe_search():
    if 'keyword' not in request.args:
        return "No keyword found."
    return f"Keyword: {request.args['keyword']}"

# 4. List all query parameters in HTML
@app.route('/all-params')
def all_params():
    html = "<ul>"
    for key, value in request.args.items():
        html += f"<li>{key} : {value}</li>"
    html += "</ul>"
    return html

# 5. /greet?name=John (use query param instead of route)
@app.route('/greet')
def greet_user():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"

# 6. /profile?mode=admin (optional query param)
@app.route('/profile-view')
def profile_view():
    mode = request.args.get('mode', 'normal')
    return f"Viewing profile in {mode} mode"

# 7. Show length of request.args
@app.route('/args-length')
def args_length():
    return f"Total query parameters: {len(request.args)}"

# 8. Show query params as an HTML table
@app.route('/args-table')
def args_table():
    html = "<table border='1'><tr><th>Key</th><th>Value</th></tr>"
    for key, value in request.args.items():
        html += f"<tr><td>{key}</td><td>{value}</td></tr>"
    html += "</table>"
    return html

# 9. /debug-check?debug=true
@app.route('/debug-check')
def debug_check():
    if request.args.get('debug') == 'true':
        return "Debugging mode ON"
    return "Debugging mode OFF"

# 10. /display/<username>?age=25
@app.route('/display/<username>')
def display(username):
    age = request.args.get('age')
    return f"User: {username}, Age: {age}" if age else f"User: {username}, Age not specified"
