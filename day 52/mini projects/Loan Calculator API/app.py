from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
api = Api(app)

def calculate_emi(amount, interest_rate, years):
    monthly_rate = (interest_rate / 100) / 12
    months = years * 12
    emi = (amount * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return round(emi, 2)

class LoanCalculator(Resource):
    def post(self):
        data = request.get_json()

        for field in ['amount', 'interest', 'years']:
            if field not in data:
                raise BadRequest(f"Field '{field}' is required.")

        try:
            amount = float(data['amount'])
            interest = float(data['interest'])
            years = int(data['years'])

            if amount <= 0 or interest <= 0 or years <= 0:
                raise ValueError
        except ValueError:
            raise BadRequest("All fields must be positive numbers.")

        emi = calculate_emi(amount, interest, years)

        return {
            "amount": amount,
            "interest_rate": interest,
            "years": years,
            "monthly_emi": emi
        }, 200

# Register route
api.add_resource(LoanCalculator, '/loan/calculate')

if __name__ == '__main__':
    app.run(debug=True)
