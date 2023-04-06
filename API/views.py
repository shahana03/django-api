from django.shortcuts import render
import requests
def index(request):
    response=requests.get( 'https://fakestoreapi.com/products')
    posts=response.json()
    
    return render(request,"index.html",{'posts':posts})
