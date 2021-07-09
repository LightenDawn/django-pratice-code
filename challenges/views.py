from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "It's the vegetarian month!"
    elif month == "february":
        challenge_text = "Remember, happy new year and happy valentines day!"
    elif month == "march":
        challenge_text = "Good good eat, good to sleep."
    elif month == "april":
        challenge_text = "First time to print hello world."
    elif month == "may":
        challenge_text = "May day, medic."
    elif month == "june":
        challenge_text = "Soon to welcome the summer vacation."
    elif month == "july":
        challenge_text = "You need to improve your coding technique and the proposal content."
    elif month == "august":
        challenge_text = "Oh no, it's time to go to school."
    elif month == "september":
        challenge_text = "The worst time ever."
    elif month == "october":
        challenge_text = "Fight, fight, fight for your life!"
    elif month == "november":
        challenge_text = "Keep going on, kid!"
    elif month == "december":
        challenge_text = "The last mile to the goal."
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)