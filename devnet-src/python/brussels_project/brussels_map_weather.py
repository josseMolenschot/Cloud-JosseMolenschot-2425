from flask import Flask, render_template
import requests

app = Flask(__name__)

# OpenWeatherMap API Configuration
API_KEY = '9240e9be1ea9f6bb8221b1bf60372cf4'  # Replace with your OpenWeatherMap API key
CITY_NAME = 'Brussels'
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'


# Fetch weather data from OpenWeatherMap API
def get_weather_data():
    params = {
        'q': CITY_NAME,
        'appid': API_KEY,
        'units': 'metric'  # To get temperature in Celsius
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None


@app.route('/')
def home():
    # Render the homepage with the Brussels map
    return render_template('home.html')


@app.route('/weather')
def weather():
    # Get weather data for Brussels
    weather_data = get_weather_data()

    if weather_data:
        # Extract weather information for today and the next 2 days
        today_weather = weather_data['list'][0]
        next_day_weather = weather_data['list'][8]  # Weather 24 hours from now
        second_day_weather = weather_data['list'][16]  # Weather 48 hours from now

        # Prepare weather info to pass to the template
        weather_info = {
            'today': {
                'temp': today_weather['main']['temp'],
                'description': today_weather['weather'][0]['description'],
                'date': today_weather['dt_txt']
            },
            'next_day': {
                'temp': next_day_weather['main']['temp'],
                'description': next_day_weather['weather'][0]['description'],
                'date': next_day_weather['dt_txt']
            },
            'second_day': {
                'temp': second_day_weather['main']['temp'],
                'description': second_day_weather['weather'][0]['description'],
                'date': second_day_weather['dt_txt']
            }
        }

        return render_template('weather.html', weather_info=weather_info)

    else:
        return 'Error fetching weather data.'


if __name__ == '__main__':
    app.run(debug=True)
