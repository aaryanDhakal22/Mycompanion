from django.shortcuts import render, redirect


from .chapters import *
from playsound import playsound
from .ai_stuff import *

import os

from homepage import sentiment_handler

# Creafte your views here.


def moodpage(request, mood):
    return render(request, "text.html")


def process(text):
    return "test", "choices"


def start_demo(request):
    pass


def homepage(request):
    if request.method == "POST":
        # print(request.POST.get("test", None))
        starter.pos += 1
    context = {}
    if not (starter.is_done):
        context = starter.return_info()
        if context["is_button"] == True:
            if context["button_count"] == 1:
                return render(request, "button.html", context)
            if context["button_count"] == 3:
                return render(request, "buttons3.html", context)
            else:
                return render(request, "choices.html", context)
        else:
            return render(request, "text.html", context)
    # return render(request, "button.html")

    # context = {"first_btn": "I'm sad"}

    # if request.method == "POST":
    #     text = request.POST["text_input"]
    #     context.setdefault("text", moodpage(request, text))
    # context.setdefault("text", "Hello there! \n How are you feeling right now?")

    # return render(request, "text.html", context)