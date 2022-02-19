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


def moodpage(requests, md):
    print(md)
    return render(requests, "home.html")


# TODO: add more (complex) emotions to allow for better interactions
# TODO: feed the currentEmotion inputs into a NN that predicts emotional state
# a var that measures the child's current emotional state
# giving the Avatar an idea of how to respond
# on a scale of zero to one how [happy, sad] the child is
currentEmotion = [0, 0]

## input => outputs

# find keywords that indicate emotion, update currentEmotion
def markEmotion(request, text):

    word_list = text.split(" ")
    emotionSum = currentEmotion[0] + currentEmotion[1]

    if "happy" in word_list:
        currentEmotion[0] = (1 + (currentEmotion[0])) / (emotionSum + 1)

    if "sad" in word_list:
        currentEmotion[1] = (1 + (currentEmotion[1])) / (emotionSum + 1)


def homepage(request):
    context = {}

    if request.method == "POST":
        text = request.POST["inp"]
        context.setdefault("text", process(request, text))

    return render(request, "home.html", context)
