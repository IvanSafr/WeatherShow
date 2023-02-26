from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
# Create your views here.


def main(request):
    #appid = "6d55abc0d37e67b465e9ee20f6d69931"  # Мой ключ не работает из-за блокировки в РФ
    appid = "0fedf62a4b48093d0fe6e0b95fe05ae2"  # Ключ преподавателя OVERONE
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+ appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    all_cities=[]
    cities = City.objects.filter().order_by('-id')[:4]

    for city in cities:
        res = requests.get(url.format(city))
        data = res.json()

        city_info = {
            'city': city.name,
            'temp': round(data["main"]['temp']),
            'weath':data["weather"][0]["description"],
            "wind": round(data["wind"]['speed']),
            'icon': data["weather"][0]['icon']
        }

        all_cities.append(city_info)

        if len(all_cities)>4:
            all_cities.pop(0)

    print(all_cities)

    context = {
        "all_info": all_cities[1:],
        "l_info": all_cities[0],
        "form": form
        }

    return render(request, 'page.html', context)