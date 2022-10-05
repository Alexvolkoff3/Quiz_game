import requests
paramis = {
    'amount': 10,
    'type': 'boolean',
}

responce = requests.get('https://opentdb.com/api.php', params=paramis)
responce.raise_for_status()
data = responce.json()
question_data = data['results']

