import requests

nameUrl = "https://playground.learnqa.ru/api/get_text"

reasponce = requests.get(nameUrl)

print(reasponce.text)