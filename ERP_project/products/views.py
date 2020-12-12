from django.shortcuts import render ,HttpResponse

# Create your views here.

def products_home(request):
    return HttpResponse("Products page")