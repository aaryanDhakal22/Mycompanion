import random


def handler(major_sentiment):
    positive_response_list = ["That's very nice", "I'm happy you are feeling good"]
    negative_response_list = ["I'm sorry to hear that", "Tell me about that"]
    neutral_response_list = [
        "Thank you for sharing",
        "Well I'm happy we have time to talk",
    ]

    if major_sentiment.lower() == "positive":
        return random.choice(positive_response_list)
    if major_sentiment.lower() == "negative":
        return random.choice(negative_response_list)
    if major_sentiment.lower() == "neutral":
        return random.choice(neutral_response_list)
