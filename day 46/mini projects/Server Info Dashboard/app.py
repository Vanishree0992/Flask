from flask import Flask, request
import os

app = Flask(__name__)

# Route: /
@app.route('/')
def server_info():
    # Get client IP address
    client_ip = request.remote_addr

    # Get port (Flask doesn't expose port directly; we hardcode what we run it on)
    port = 8000

    # Get environment (development/production)
    flask_env = os.getenv('FLASK_ENV', 'production')

    return f"""
    <html>
      <body>
        <h1>Server Info Dashboard</h1>
        <p><b>Client IP:</b> {client_ip}</p>
        <p><b>Server Port:</b> {port}</p>
        <p><b>Environment:</b> {flask_env}</p>
      </body>
    </html>
    """

# Route: /status
@app.route('/status')
def status():
    debug_mode = app.debug
    if debug_mode:
        return "Running in Debug Mode"
    else:
        return "Running in Production Mode"

if __name__ == '__main__':
    # Manually set port to 8000
    app.run(debug=True, port=8000)

# with system info
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def server_info():
    ip = request.remote_addr
    port = request.environ.get('SERVER_PORT', 'unknown')
    debug_mode = app.debug
    env = os.environ.get('FLASK_ENV', 'production')

    return f"""
    <html>
      <body style="font-family: Arial;">
        <h2>Server Info Dashboard</h2>
        <ul>
          <li><b>Client IP:</b> {ip}</li>
          <li><b>Server Port:</b> {port}</li>
          <li><b>Environment:</b> {env}</li>
          <li><b>Debug Mode:</b> {'Enabled' if debug_mode else 'Disabled'}</li>
        </ul>
      </body>
    </html>
    """

@app.route('/status')
def status():
    if app.debug:
        return "<p style='color: green;'>Running in Debug Mode</p>"
    else:
        return "<p style='color: red;'>Running in Production Mode</p>"

if __name__ == '__main__':
    # Run on custom port 8000
    app.run(debug=os.getenv("FLASK_DEBUG") == "1", port=8000)
