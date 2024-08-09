from flask import Flask, render_template
from api_client import weather_api_client
from datetime import datetime
import json

app = Flask(__name__)


def format_datetime(value):
    return datetime.fromtimestamp(value)

app.jinja_env.filters['format_dt'] = format_datetime

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather/<city>')
def weather(city):
    wapi = weather_api_client()
    try:
        data = wapi.get_weather(city)
        return render_template('weather.html', city_name=city, weather_data=json.loads(data))
    except:
        print('Unable to get weather data. Reading from file...')
        # read file
        with open('weather_data.json', 'r') as myfile:
            data = myfile.read()
        return render_template('weather.html', city_name=city, weather_data=json.loads(data))


@app.route('/forecast/<city>')
def forecast(city):
    wapi = weather_api_client()
    try:
        data = wapi.get_forecast(city)
        return render_template('forecast.html', city_name=city, forecast_data=json.loads(data))
    except:
        print('Unable to get forecast data. Reading from file...')
        # read file
        with open('forecast_data.json', 'r') as myfile:
            data = myfile.read()
        return render_template('forecast.html', city_name=city, forecast_data=json.loads(data))

def get_datetime_from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
