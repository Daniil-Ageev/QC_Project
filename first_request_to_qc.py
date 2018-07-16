import requests
from requests.auth import HTTPBasicAuth

url = "https://almalmqc1250saastrial.saas.hpe.com"
login = ""
password = ""
cookies = dict()
headers = {}

r = requests.get(url + "/qcbin/rest/is-authenticated")
print(r.status_code, r.headers.get('WWW-Authenticate'))

r = requests.get(url + "/qcbin/authentication-point/authentication",
                 auth=HTTPBasicAuth(almUserName, almPassword), headers=headers)
print(r.status_code, r.headers)

cookie = r.headers.get('Set-Cookie')
LWSSO_COOKIE_KEY = cookie[cookie.index("=") + 1: cookie.index(";")]
cookies['LWSSO_COOKIE_KEY'] = LWSSO_COOKIE_KEY
print(cookies)

r = requests.post(url + "/qcbin/rest/site-session", cookies=cookies)
print(r.status_code, r.headers)
