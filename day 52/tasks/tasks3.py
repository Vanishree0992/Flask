from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# 1–5. JSON Echo Route
@app.route('/api/echo', methods=['POST'])
def echo():
    # 2. Handle None if content-type is not JSON
    if not request.is_json:
        return jsonify({'status': 'error', 'message': 'Content-Type must be application/json'}), 400

    # 1. Safely extract JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'status': 'error', 'message': 'Invalid JSON data'}), 400

    # 3. Access nested fields
    bio = data.get('user', {}).get('profile', {}).get('bio', 'N/A')

    print(f"Bio received: {bio}")  # Logging

    # 4. Echo the received JSON
    return jsonify({'status': 'success', 'received': data}), 200

# 6–7. Multiply Route
@app.route('/api/multiply', methods=['POST'])
def multiply():
    if not request.is_json:
        return jsonify({'status': 'error', 'message': 'Content-Type must be application/json'}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 400

    x = data.get('x')
    y = data.get('y')

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return jsonify({'status': 'error', 'message': 'x and y must be numbers'}), 400

    product = x * y
    return jsonify({'status': 'success', 'result': product}), 200

# 10. Compare json.loads(request.data)
@app.route('/api/compare', methods=['POST'])
def compare_methods():
    try:
        # Using get_json()
        parsed_json = request.get_json()
        
        # Using json.loads()
        raw_data = request.data
        loaded_json = json.loads(raw_data)

        return jsonify({
            'status': 'success',
            'request.get_json': parsed_json,
            'json.loads': loaded_json
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


# 9. Differences Between Formats:
# Format	Use Case	request.get_json() Works?
# raw (JSON)	Preferred for APIs	✅ Yes
# form-data	Used for file uploads or forms	❌ No
# x-www-form-urlencoded	Web forms (e.g., login forms)	❌ No