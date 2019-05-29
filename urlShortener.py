import requests
import simplejson as json

# https://developers.google.com/url-shortener/v1/getting_started
# 위 사이트를 가지고 JSON데이터의 입출력이 웹에서 어떻게 일어나는지 보여준다.
#

url = "https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "http://www.google.com/"}
headers = {"Content-Type": "application/json"}

r = requests.post(url, json=payload, headers=headers)

print("Status Code:", r.status_code)
print("============================")
print(r.headers)
print("============================")
print(r.text)
