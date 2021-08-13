import requests
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class City(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def first() :
    url = ''
    if request.method == 'POST' :
        new_city = request.form['city']

        if new_city :
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={YOUR API KEY}'

    cities = City.query.all()

    weather_data = []

    for city in cities :
        r = requests.get(url.format(city.name)).json()
        sunr = r['sys']['sunrise']
        sunrise = datetime.fromtimestamp(sunr)
        suns = r['sys']['sunset']
        sunset = datetime.fromtimestamp(suns)

        weather = {
            'city' : city.name,
            'id' : city.id,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'humidity' : r['main']["humidity"],
            'pressure' : r['main']["pressure"],
            'winds' : r['wind']["speed"],
            'windd' : r['wind']["deg"],
            'visibility' : r['visibility'],
            'clouds' : r['clouds']['all'],
            'country' : r['sys']['country'],
            'low' : r['main']["temp_min"],
            'high' : r['main']["temp_max"],
            'feel' : r['main']["feels_like"],
            'sunrise' : sunrise,
            'sunset' : sunset,
            'unit' : 'C'

        }

        weather_data.append(weather)

    return render_template('index.html', weather_data=weather_data)


@app.route('/imperial', methods=['GET', 'POST'])
def second() :
    url = ''
    if request.method == 'POST' :
        new_city = request.form['city']

        if new_city :
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={YOU API KEY}'

    cities = City.query.all()

    weather_data = []

    for city in cities :
        r = requests.get(url.format(city.name)).json()
        sunr = r['sys']['sunrise']
        sunrise = datetime.fromtimestamp(sunr)
        suns = r['sys']['sunset']
        sunset = datetime.fromtimestamp(suns)

        weather = {
            'city' : city.name,
            'id' : city.id,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'humidity' : r['main']["humidity"],
            'pressure' : r['main']["pressure"],
            'winds' : r['wind']["speed"],
            'windd' : r['wind']["deg"],
            'visibility' : r['visibility'],
            'clouds' : r['clouds']['all'],
            'country' : r['sys']['country'],
            'low' : r['main']["temp_min"],
            'high' : r['main']["temp_max"],
            'feel' : r['main']["feels_like"],
            'sunrise' : sunrise,
            'sunset' : sunset,
            'unit' : 'F'

        }

        weather_data.append(weather)

    return render_template('imperial.html', weather_data=weather_data)


@app.route('/delete/<int:id>')
def delete(id) :
    alltodo = City.query.filter_by(id=id).first()
    db.session.delete(alltodo)
    db.session.commit()
    return redirect('/')


@app.route('/api')
def apo() :
    return render_template('api.html')

#TO CREATE REST API
@app.route('/api/metric/<string:city>')
def apoc(city) :
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={YOU API KEY}'

    r = requests.get(url.format(city)).json()
    return r


@app.route('/api/imperial/<string:city>')
def apof(city) :
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={YOU API KEY}'

    r = requests.get(url.format(city)).json()
    return r

# write debug=False while in production and remove port number
if __name__ == "__main__" :
    app.run(debug=True, port=3700)
