from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def index_view(request):
    # API Endpoint
    URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(URL).json()

    return HttpResponse(data)
