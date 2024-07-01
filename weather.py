
from flask import Flask, render_template, request
app = Flask(__name__)
api_url = ('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric')
api_key = 'be77a197be3be860ee50beb28b07040d'

def query_api(city):
    try:
        print(api_url.format(city, api_key))
        r = request.get(api_url.format(city, api_key)).json()
        return r
    except :

        return None
app.route('/')
def index():
      city ="newyork"
      weather = query_api(city)
      return render_template('weatherin.html',city=city, weather=weather)
if __name__ == '__main__':
    app.run(debug=True)