from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month
        })
    except:
        raise Http404()
