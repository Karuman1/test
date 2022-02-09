import requests

url = "https://evilinsult.com/generate_insult.php"

response = requests.get(url, params={'lang': 'ru', 'type': 'json'})

print(response.json()['insult'])
