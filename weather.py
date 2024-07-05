
from flask import Flask, render_template, request
app = Flask(__name__)
import requests
api_url = ('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric')
api_key = 'be77a197be3be860ee50beb28b07040d'

def query_api(city):
    try:
        print(api_url.format(city, api_key))
        r = requests.get(api_url.format(city, api_key)).json()
        return r
    except :

        return None
@app.route('/')
def index():
      city ="Indonesia"
      resp = query_api(city)
      country=resp['sys']['country']
      hmd= resp['main']['humidity']
      temp=resp['main']['temp']
      weater=resp['weather'][0]['description']
      icon=resp['weather'][0]['icon']
      print(weater)
      print(temp)
      print(hmd)
      return render_template('weatherin.html',city=city, weather=weater, country=country, hmd=hmd,
      temp=temp, weater=weater, icon=icon)
@app.route('/result', methods=['GET','POST'])
def result():

        city = request.form.get('city')
        resp = query_api(city)
        temp=resp['main']['temp']
        hmd = resp['main']['humidity']
        weater = resp['weather'][0]['description']
        icon = resp['weather'][0]['icon']
        return render_template('weatherin.html',city=city, weather=weater, temp=temp, hmd=hmd, weater=weater, icon=icon)

if __name__ == '__main__':
    app.run(debug=True)