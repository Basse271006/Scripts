import json
import requests

class bcolors:
    OKBLUE = '\033[94m'

requestUrl = 'http://ipinfo.io'

r = requests.get(requestUrl)

data = json.loads(r.text)

print(f'{bcolors.OKBLUE}Din IP adresse er: ' + data['ip'])
