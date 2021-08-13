Weather pin web app made using flask also has capability to provide api further to be used without key
This app is live in Heroku server


You can access the Json data through below RESTAPI's url without using key (Only for learning purposes)

Metric Data :
https://pinweather.herokuapp.com/api/metric/{CITY_NAME}

Imperial Data :
https://pinweather.herokuapp.com/api/imperial/{CITY_NAME}

Original URL of Open weather api :
http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&units={imperial/metric}&appid={YOUR API KEY}

JSON FORMAT :
                    {
                        "base": "stations",
                        "clouds": {
                        "all": 95
                        },
                        "cod": 200,
                        "coord": {
                        "lat": 30.8344,
                        "lon": 76.9333
                        },
                        "dt": 1628836926,
                        "id": 1268381,
                        "main": {
                        "feels_like": 87.03,
                        "grnd_level": 933,
                        "humidity": 51,
                        "pressure": 1003,
                        "sea_level": 1003,
                        "temp": 85.23,
                        "temp_max": 85.23,
                        "temp_min": 85.23
                        },
                        "name": "london",
                        "sys": {
                        "country": "IN",
                        "id": 9181,
                        "sunrise": 1628813834,
                        "sunset": 1628861836,
                        "type": 1
                        },
                        "timezone": 19800,
                        "visibility": 10000,
                        "weather": [
                        {
                        "description": "overcast clouds",
                        "icon": "04d",
                        "id": 804,
                        "main": "Clouds"
                        }
                        ],
                        "wind": {
                        "deg": 256,
                        "gust": 6.76,
                        "speed": 4.03
                        }
                        }
                        
                        

