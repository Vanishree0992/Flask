from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for goals
goals = []

@app.route('/')
def home():
    return '''
    <h2>Fitness Goal Tracker</h2>
    <form method="POST" action="/goal-submit">
        Name: <input type="text" name="name" required><br><br>
        Goal Type:
        <select name="goal_type">
            <option value="weight">Weight Loss</option>
            <option value="muscle">Muscle Gain</option>
            <option value="cardio">Cardio Fitness</option>
        </select><br><br>
        <button type="submit">Submit Goal</button>
    </form>
    <br>
    <a href="/goals?type=weight">View Weight Goals</a>
    '''

@app.route('/goal-submit', methods=['POST'])
def submit_goal():
    name = request.form.get('name')
    goal_type = request.form.get('goal_type')

    goals.append({'name': name, 'goal_type': goal_type})
    return redirect(url_for('goal_status', name=name))

@app.route('/goal-status/<name>')
def goal_status(name):
    return f"<h3>Hi {name}, your fitness goal has been recorded!</h3>"

@app.route('/goals')
def filter_goals():
    goal_type = request.args.get('type')
    filtered_goals = [g for g in goals if g['goal_type'] == goal_type] if goal_type else goals

    if not filtered_goals:
        return "<p>No goals found for this type.</p>"

    goal_list = ''.join(
        f"<li>{g['name']} - {g['goal_type'].capitalize()} Goal</li>" for g in filtered_goals
    )
    return f"<h3>Goals for {goal_type.capitalize() if goal_type else 'All'}:</h3><ul>{goal_list}</ul>"

if __name__ == '__main__':
    app.run(debug=True)
