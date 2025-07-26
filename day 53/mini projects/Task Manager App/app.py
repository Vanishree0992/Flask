from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
tasks = [
    {"id": 1, "title": "Buy groceries"},
    {"id": 2, "title": "Finish homework"}
]

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks, title="Task Manager")

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    new_task = {"id": new_id, "title": data.get("title")}
    tasks.append(new_task)
    return jsonify({"message": "Task added", "task": new_task}), 201

if __name__ == '__main__':
    app.run(debug=True)
