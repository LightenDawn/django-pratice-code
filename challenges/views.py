from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "It's the vegetarian month!",
    "february": "Remember, happy new year and happy valentines day!",
    "march": "Good good eat, good to sleep.",
    "april": "First time to print hello world.",
    "may": "May day, medic.",
    "june": "Soon to welcome the summer vacation.",
    "july": "You need to improve your coding technique and the proposal content.",
    "august": "Oh no, it's time to go to school.",
    "september": "The worst time ever.",
    "october": "Fight, fight, fight for your life!",
    "november": "Keep going on, kid!",
    "december": "The last mile to the goal."
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
