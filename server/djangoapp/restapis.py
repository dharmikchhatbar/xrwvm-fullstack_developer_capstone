import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    request_url = backend_url + endpoint
    if params:
        request_url += "?" + params.rstrip("&")

    print(f"Calling backend_url: {request_url}")  # Debug print

    try:
        response = requests.get(request_url)
        print(f"Response Status Code: {response.status_code}")  # Debug print
        print(f"Response Content: {response.text}")  # Debug print
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {"error": "Network exception occurred"}


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    print(f"Analyzing sentiment at {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"error": "Network exception occurred"}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return {"error": "Network exception occurred"}
