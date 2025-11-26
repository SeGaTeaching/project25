from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests

# Create your views here.
def index(request):
    
    API_KEY = settings.WEATHER_API
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY
    
    if 'city' in request.GET:
        city_name = request.GET.get('city')
        
        response = requests.get(url.format(city_name))
        if response.status_code == 200:
            data = response.json()
            weather = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            return render(request, 'weather/index.html', {'weather': weather})
        else:
             return render(request, 'weather/index.html', {'error': 'Stupid, that is nor a real place!'})
        
    
    return render(request, 'weather/index.html')
