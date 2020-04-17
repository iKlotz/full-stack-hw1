from flask import Flask, send_file
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/weather/<city>')
def weather(city):
    secret = '51f7a66f03c8df5b96089f58bfb51cd0'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': secret}
    response = requests.get(url=url, params=params)
    temp = str(response.json()['main']['temp'])
    return 'Temperature in ' + city + ' is: ' + temp + get_gif(temp)


def get_gif(temp):
    secret = 'PWlp52TJObygYRbo50orNSAVY8EYLwsq'
    url = 'https://api.giphy.com/v1/gifs'

    if float(temp) > 21:
        ids = 'Lopx9eUi34rbq'
    elif float(temp) > 0:
        ids = '9JwU9SBhaNQNCuoQBc'
    else:
        ids = 's4Bi420mMDRBK'

    param = {'ids': ids, 'api_key': secret}
    response = requests.get(url=url, params=param)
    image = "<br><img src=" + str(response.json()['data'][0]['images']['downsized']['url']) + ">"

    return image


if __name__ == '__main__':
    app.run()
