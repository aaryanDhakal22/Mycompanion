from django.shortcuts import render, redirect
from homepage.models import MinorUser, DiaryEntry
from homepage.ai_stuff.ai import demo_sentiment_provider, sentiment_provider_with_ai
from .sentiment_handler import handler
from playsound import playsound


def startpage(request):
    return render(request, "frame1.html")


def frames(request, id):
    html_curr = "frame" + str(id) + ".html"
    return render(request, html_curr)


def names(request):
    name = request.POST["user_name"]
    user_ = MinorUser.objects.create(name=name)
    return render(request, "frame4.html", {"user": user_})


def diary(request):
    print(request.method)
    happy = request.POST["happy"]
    stress = request.POST["stress"]
    energy = request.POST["energy"]

    DiaryEntry.objects.create(happiness=happy, stress=stress, energy=energy)
    return render(request, "frame5.html")


def start(request):
    return render(request, "main.html")


def analyze(request):
    path_to_audio = "D:/Projects/Mycompanion/mycp/homepage/audio/short_audio.wav"
    playsound(path_to_audio)
    # sentiment = sentiment_provider_with_ai(path_to_audio)  # full version
    sentiment = demo_sentiment_provider(path_to_audio)  # without api
    final_text_for_demo = handler(sentiment)
    return render(
        request, "main2.html", context={"final_text_for_demo": final_text_for_demo}
    )
