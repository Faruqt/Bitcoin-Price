import requests
from django.shortcuts import render

# Create your views here.

def chart(request):
    response = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?start=2021-09-08&end=2021-09-17&index=[USD]')
    price = response.json()
    return render(request, "btc/chart.html", {"price": price})
