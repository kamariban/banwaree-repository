import requests

def get_advice():
    url = "https://api.adviceslip.com/advice"

    response = requests.get(url)
    data = response.json()

    return data["slip"]["advice"]

print(get_advice())
