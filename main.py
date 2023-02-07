import requests

TOKEN = '5661659754:AAGPPm7mkuylCre31dUmOBcXN3cgULdoqSQ'
# url getUpdates
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
response = requests.get(url)
data = response.json()
chat_id = data['result'][0]['message']['chat']['id']

print(chat_id)