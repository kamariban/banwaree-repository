import requests

def get_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url)
    data = response.json()

    return data["message"]

print(get_dog_image())