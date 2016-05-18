import requests
session = requests.session()

params = {'username' : 'Kevin', 'password' : 'password'}
url = 'http://pythonscraping.com/pages/cookies/welcome.php'
s = session.post(url, data = params)

print(s.cookies.get_dict())

url = 'http://pythonscraping.com/pages/cookies/profile.php'
s = session.get(url)
print(s.text)