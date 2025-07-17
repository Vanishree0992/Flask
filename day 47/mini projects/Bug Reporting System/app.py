from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
app.config['DEBUG'] = True

# Store bug reports in memory (temporary)
bugs = []
bug_id_counter = 1

@app.route("/report", methods=["GET", "POST"])
def report_bug():
    if request.method == "POST":
        global bug_id_counter
        title = request.form.get("title")
        desc = request.form.get("description")
        priority = request.form.get("priority")

        bug = {
            "id": bug_id_counter,
            "title": title,
            "description": desc,
            "priority": priority
        }
        bugs.append(bug)
        bug_id_counter += 1
        return redirect(url_for("report_confirm"))

    return '''
        <h2>Bug Report Form</h2>
        <form method="POST">
            Title: <input type="text" name="title" required><br><br>
            Description:<br>
            <textarea name="description" required></textarea><br><br>
            Priority:
            <select name="priority">
                <option>low</option>
                <option>medium</option>
                <option>high</option>
            </select><br><br>
            <button type="submit">Submit Bug</button>
        </form>
        <br><a href="/bugs">View All Bugs</a>
    '''

@app.route("/submit-report")
def report_confirm():
    return "<h3>Bug report submitted successfully!</h3><br><a href='/bugs'>View All Bugs</a>"

@app.route("/bugs")
def view_bugs():
    priority_filter = request.args.get("priority")
    filtered = [b for b in bugs if b["priority"] == priority_filter] if priority_filter else bugs

    html = "<h2>Reported Bugs</h2><ul>"
    for b in filtered:
        html += f"<li><a href='/bug/{b['id']}'>Bug #{b['id']} - {b['title']} ({b['priority']})</a></li>"
    html += "</ul>"

    html += '''
        <form method="get">
            <label>Filter by Priority:</label>
            <select name="priority">
                <option>low</option>
                <option>medium</option>
                <option>high</option>
            </select>
            <button type="submit">Filter</button>
        </form>
        <br><a href="/report">Report Another Bug</a>
    '''
    return html

@app.route("/bug/<int:id>")
def bug_detail(id):
    bug = next((b for b in bugs if b["id"] == id), None)
    if not bug:
        return "<h3>Bug not found!</h3>", 404

    return f'''
        <h2>Bug Details</h2>
        <strong>Bug #{bug["id"]}</strong><br>
        <strong>Title:</strong> {bug["title"]}<br>
        <strong>Description:</strong> {bug["description"]}<br>
        <strong>Priority:</strong> {bug["priority"]}<br><br>
        <a href="/bugs">Back to List</a>
    '''

if __name__ == "__main__":
    app.run()
