import random as rd


def handler(major_sentiment):
    pos = "oh thats nice . wow fantastic"
    neg = ""
    neut = ""
    pos = pos.split(".")
    neg = neg.split(".")
    neut = neut.split(".")

    if major_sentiment.lower() == "positive":
        return rd.choice([pos])
    if major_sentiment.lower() == "negative":
        return rd.choice([neg])
    if major_sentiment.lower() == "neutral":
        return rd.choice([neut])
    