from django.shortcuts import render, redirect
from .chapters import *

# Create your views here.


def moodpage(request, mood):
    return render(request, "text.html")


def process(text):
    return "test", "choices"


def homepage(request):
    if request.method == "POST":
        # print(request.POST.get("test", None))
        starter.pos += 1
    context = {}
    if not (starter.is_done):

        if request.POST.get("text_input", None) != None:
            reply_by_user = request.POST["text_input"]

            if starter.name == None:
                starter.name = reply_by_user
                starter.is_done = True
            else:
                reply, return_type = process(reply_by_user)

                if return_type == "choices":
                    return render(request, "choices.html")
        else:
            context = starter.return_info()
            if context["is_button"] == True:
                if context["button_count"] == 1:
                    return render(request, "button.html", context)
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
