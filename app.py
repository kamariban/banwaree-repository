import requests

def get_fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"

    response = requests.get(url)
    data = response.json()

    return data["text"]

print("Random fact:", get_fact())