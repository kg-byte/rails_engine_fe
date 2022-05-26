from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.
def merchants(request):
  response = requests.get('http://localhost:3000/api/v1/merchants')
  merchants = response.json()
  # import ipdb; ipdb.set_trace()
  return render(request, "merchants.html", {'merchants': merchants['data']})
  pass

def merchant(request, merchant_id):
  response1 = requests.get("http://localhost:3000/api/v1/merchants/{merchant_id}".format(merchant_id=merchant_id))
  response2 = requests.get("http://localhost:3000/api/v1/merchants/{merchant_id}/items".format(merchant_id=merchant_id))
  merchant = response1.json()
  merchantItems = response2.json()
  return render(request, "merchantItems.html", {'merchant': merchant['data'], 
  												'merchantItems': merchantItems['data']})

def item(request, item_id):
  response = requests.get("http://localhost:3000/api/v1/items/{item_id}".format(item_id=item_id))
  item = response.json()
  return render(request, "item.html", {'item': item['data']})


def items(request):
  response = requests.get("http://localhost:3000/api/v1/items")
  items = response.json()
  return render(request, "items.html", {'items': items['data']})


def search(request):
  name = request.GET.get('search')
  if name == '':
    merchants = 'N/a'
  else:
    response = requests.get("http://localhost:3000/api/v1/merchants/find_all?name={name}".format(name=name))
    merchants=response.json()['data']
  return render(request, "searchMerchants.html", {'merchants': merchants,
  												  'keyword': name})
