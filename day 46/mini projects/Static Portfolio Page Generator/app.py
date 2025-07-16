from flask import Flask

app = Flask(__name__)

# Mock data for demonstration
skills_data = {
    "john": ["Python", "Flask", "HTML", "CSS"],
    "jane": ["Java", "Spring", "SQL", "AWS"]
}

projects_data = {
    "john": [
        {"name": "Website Redesign", "year": 2023, "status": "Completed"},
        {"name": "API Development", "year": 2024, "status": "In Progress"}
    ],
    "jane": [
        {"name": "Mobile App", "year": 2023, "status": "Completed"},
        {"name": "Database Migration", "year": 2024, "status": "Planned"}
    ]
}

# /portfolio/<name>
@app.route('/portfolio/<string:name>')
def portfolio(name):
    return f"""
    <html>
      <body>
        <h1>Portfolio for {name.title()}</h1>
        <p>Welcome to {name.title()}'s personal portfolio page.</p>
        <hr>
        <p>Check out:
          <a href="/portfolio/{name}/skills">Skills</a> |
          <a href="/portfolio/{name}/projects">Projects</a>
        </p>
      </body>
    </html>
    """

# /portfolio/<name>/skills
@app.route('/portfolio/<string:name>/skills')
def skills(name):
    skills = skills_data.get(name.lower(), [])
    skills_list = "".join(f"<li>{skill}</li>" for skill in skills) if skills else "<li>No skills found.</li>"

    return f"""
    <html>
      <body>
        <h1>{name.title()}'s Skills</h1>
        <ul>{skills_list}</ul>
        <p><a href="/portfolio/{name}">Back to Profile</a></p>
      </body>
    </html>
    """

# /portfolio/<name>/projects
@app.route('/portfolio/<string:name>/projects')
def projects(name):
    projects = projects_data.get(name.lower(), [])
    if not projects:
        table_rows = "<tr><td colspan='3'>No projects found.</td></tr>"
    else:
        table_rows = "".join(
            f"<tr><td>{p['name']}</td><td>{p['year']}</td><td>{p['status']}</td></tr>"
            for p in projects
        )

    return f"""
    <html>
      <body>
        <h1>{name.title()}'s Projects</h1>
        <table border="1" cellpadding="5" cellspacing="0">
          <tr>
            <th>Project Name</th>
            <th>Year</th>
            <th>Status</th>
          </tr>
          {table_rows}
        </table>
        <p><a href="/portfolio/{name}">Back to Profile</a></p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
