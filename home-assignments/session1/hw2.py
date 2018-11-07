import requests

mygeolocation = requests.get('http://ip-api.com/json')
data1 = mygeolocation.json()
city = data1.get('city')
country = data1.get('country')
weathreq = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID='
                        '7ef1d0ff2e38b229d669d944b8ea4990')
data2 = weathreq.json()
weather = data2.get('weather', 'main')
weather = weather[0]
weather = weather.get('description')
temp = data2.get('main')
temp = temp.get('temp')
print('Current weather in ', city, ' ,', country, ':', weather, '\n', 'And the temperature is', temp, 'Degrees celsius')
