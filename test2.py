from datetime import datetime
import requests

urlo = 'http://api.openweathermap.org/data/2.5/weather?q=sydney&units=metric&appid=470551ef1a3184b421bb48e0a32b67d6'


r = requests.get(urlo).json()
f=r['timezone']
m=datetime.fromtimestamp(f)
p=m.strftime('%H:%M')
print(p)