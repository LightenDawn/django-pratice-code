from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("It's the vegetarian month!")


def february(request):
    return HttpResponse("Remember, happy new year and happy valentines day!")
