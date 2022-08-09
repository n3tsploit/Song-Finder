import requests
data = {
    'api_token': 'ecce5a249ce9ea37615b5da1249d1d5f',
    'url': '/home/digzsudi/Music/example.mp3',
    'return': 'apple_music,spotify',
}
result = requests.post('https://api.audd.io/', data=data)
print(result.text)