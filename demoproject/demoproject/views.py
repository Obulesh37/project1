from django.http import HttpResponse
from django.shortcuts import render

def index_page(request):
    return render(request,"index.html")

def about_page(request):
    return render(request,"about.html")
def shop_page(request):
    return render(request,"shop.html")
def contact_page(request):
    return render(request,"contact.html")