from flask import Flask

app = Flask(__name__)

@app.route('/calc/<op>/<float:num1>/<float:num2>')
def calculate(op, num1, num2):
    if op == "add":
        result = num1 + num2
        operation = "Addition"
    elif op == "sub":
        result = num1 - num2
        operation = "Subtraction"
    elif op == "mul":
        result = num1 * num2
        operation = "Multiplication"
    elif op == "div":
        if num2 == 0:
            return """
            <html>
              <body style="font-family: Arial; text-align: center;">
                <h2 style="color: red;">Error: Division by zero is not allowed!</h2>
              </body>
            </html>
            """
        result = num1 / num2
        operation = "Division"
    else:
        return """
        <html>
          <body style="font-family: Arial; text-align: center;">
            <h2 style="color: red;">Invalid operation! Use /ops to see valid operations.</h2>
          </body>
        </html>
        """

    return f"""
    <html>
      <body style="font-family: Arial; text-align: center;">
        <h2>Operation: {operation}</h2>
        <h2>Input: {num1} and {num2}</h2>
        <h2>Result: {result}</h2>
      </body>
    </html>
    """

@app.route('/ops')
def ops():
    return """
    <html>
      <body style="font-family: Arial; text-align: center;">
        <h2>Valid Operations</h2>
        <ul style="list-style: none; font-size: 20px;">
          <li><strong>add</strong> → Addition</li>
          <li><strong>sub</strong> → Subtraction</li>
          <li><strong>mul</strong> → Multiplication</li>
          <li><strong>div</strong> → Division</li>
        </ul>
        <p>Use format: /calc/&lt;op&gt;/&lt;num1&gt;/&lt;num2&gt;</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
