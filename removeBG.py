# Requires "requests" to be installed (see python-requests.org)
import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('./img/origin/file.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'YOURAPIKEY '},
    #headers={'X-Api-Key': ' '},
)
if response.status_code == requests.codes.ok:
    with open('./img/nobg/no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)