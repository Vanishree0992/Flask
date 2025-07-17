from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/weather', methods=['GET'])
def weather_form():
    return '''
    <h2>🌤️ Weather Report Generator</h2>
    <form method="POST" action="/weather-result">
        City: <input type="text" name="city" required><br><br>
        <button type="submit">Get Weather</button>
    </form>
    <br>
    <a href="/weather?unit=metric">View with Metric Units</a>
    '''

@app.route('/weather-result', methods=['POST'])
def weather_result():
    city = request.form.get('city')
    return redirect(url_for('weather_city', city=city))

@app.route('/weather/<city>')
def weather_city(city):
    unit = request.args.get('unit', 'standard')
    fake_weather = {
        'standard': f"The weather in {city.title()} is 86°F, clear sky.",
        'metric': f"The weather in {city.title()} is 30°C, clear sky.",
        'imperial': f"The weather in {city.title()} is 86°F, clear sky."
    }

    report = fake_weather.get(unit, fake_weather['standard'])

    return f'''
    <h3>Weather Report for {city.title()}</h3>
    <p>{report}</p>
    <a href="/weather">Back</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
