'''
    使用HTTP Basic Access Authentication
'''

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('Kevin', 'password')
r = requests.post(url = 'http://pythonscraping.com/pages/auth/login.php', auth = auth)
print(r.text)