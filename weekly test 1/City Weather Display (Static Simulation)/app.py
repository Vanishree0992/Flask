from flask import Flask, render_template, request

app = Flask(__name__)

# Simulated static weather data
weather_data = {
    'chennai': {'temp_c': 34, 'temp_f': 93, 'condition': 'sunny'},
    'mumbai': {'temp_c': 30, 'temp_f': 86, 'condition': 'cloudy'},
    'delhi': {'temp_c': 28, 'temp_f': 82, 'condition': 'rainy'},
    'kolkata': {'temp_c': 32, 'temp_f': 90, 'condition': 'sunny'},
}

@app.route('/weather/<city>')
def weather(city):
    unit = request.args.get('unit', 'celsius')
    city_lower = city.lower()
    
    data = weather_data.get(city_lower, {
        'temp_c': 'N/A', 'temp_f': 'N/A', 'condition': 'unknown'
    })
    
    if unit == 'fahrenheit':
        temperature = f"{data['temp_f']} °F"
    else:
        temperature = f"{data['temp_c']} °C"
    
    return render_template("weather.html", city=city.title(), temperature=temperature, condition=data['condition'])

if __name__ == '__main__':
    app.run(debug=True)
