from django.shortcuts import render
import requests

# Create your views here.


def index_view(request):
    # API Endpoint
    URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(URL).json()

    context = {'data': data}

    return render(request, 'positions/index.html', context)
