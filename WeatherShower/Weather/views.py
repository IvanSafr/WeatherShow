from django.shortcuts import render, redirect
import requests

# Create your views here.


def main(request):
    #appid = "6d55abc0d37e67b465e9ee20f6d69931"  # Мой ключ не работает из-за блокировки в РФ
    appid = "0fedf62a4b48093d0fe6e0b95fe05ae2"  # Ключ преподавателя OVERONE

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+ appid

    city = 'Bryansk'

    res = requests.get(url.format(city))
    #print(res.text)
    data = res.json()
    print(data)
    city_info = {
        'city': city,
        'temp': round(data["main"]['temp']),
        'weath':data["weather"][0]["description"],
        "wind": data["wind"]['speed'],
        'icon': data["weather"][0]['icon']
    }

    context = {
        "info": city_info
        }

    return render(request, 'page.html', context)