from django.shortcuts import render, redirect

# Create your views here.


def process(request, text):
    if text == "hi":
        return "hello"
    if text == "who are you":
        return "im the mystical cat of you're dreams"
    if text == "its not you're its your":
        return "its not YOUR business. Mind your own."
    if text == "im sad":
        return "lol"
    if text == "what lol":
        return "hehe"
    else:
        return "I didnt understand"


def homepage(request):
    context = {}

    if request.method == "POST":
        text = request.POST["inp"]
        context.setdefault("text", process(request, text))

    return render(request, "home.html", context)
