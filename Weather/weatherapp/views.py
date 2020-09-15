from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests


def index(request):
    appid = "afae0d910927badebe4f036fe5c2b874"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'humidity': res["main"]["humidity"],
            'wind_speed': res["wind"]["speed"]
            }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
        }

    return render(request, "weatherapp/index.html", context)

