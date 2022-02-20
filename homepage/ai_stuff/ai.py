import sys
from datetime import datetime
from random import choice

# from xxlimited import new/

# from configure import auth_key
import requests
import pprint
from time import sleep

# store globals
auth_key = "47b32e758a344b379770d421e20c95b6"
headers = {"authorization": auth_key, "content-type": "application/json"}

transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
upload_endpoint = "https://api.assemblyai.com/v2/upload"


def demo_sentiment_provider(file_path):
    return choice(["positive", "negative", "neutral"])


# Unused due to high time for taken by the assemblyAI API to return results
# OPTIONAL
def sentiment_provider_with_ai(file_path):
    # reads audio file
    def read_file(filename):
        with open(filename, "rb") as _file:
            while True:
                data = _file.read(5242880)
                if not data:
                    break
                yield data

    # upload our audio file
    upload_response = requests.post(
        upload_endpoint, headers=headers, data=read_file(file_path)
    )
    print("Audio file uploaded")

    # send a request to transcribe the audio file
    transcript_request = {
        "audio_url": upload_response.json()["upload_url"],
        "sentiment_analysis": "true",
    }
    transcript_response = requests.post(
        transcript_endpoint, json=transcript_request, headers=headers
    )
    print("Transcription Requested")
    pprint.pprint(transcript_request)
    pprint.pprint(transcript_response.json())
    prev_time = datetime.now()
    # set up polling
    polling_response = requests.get(
        transcript_endpoint + "/" + transcript_response.json()["id"], headers=headers
    )
    # filename = transcript_response.json()["id"] + ".txt"

    # if our status isn’t complete, sleep and then poll again
    while polling_response.json()["status"] != "completed":
        sleep(1)
        polling_response = requests.get(
            transcript_endpoint + "/" + transcript_response.json()["id"],
            headers=headers,
        )
        print("File is", polling_response.json()["status"])
    pprint(polling_response)
    new_time = datetime.now()
    elapsed = new_time - prev_time
    print(elapsed.seconds, ":", round(elapsed.microseconds, 2))
