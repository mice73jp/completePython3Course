import requests

# Save web page source
# r = requests.get("http://google.com")
#
# print("Status Code :", r.status_code)
#
# print(r.url)
# print(r.text)
#
# f = open("./page.html", "w+")
# f.write(r.text)

params = {"q": "pizza"}
r = requests.get("http://www.bing.com/search", params=params)
print("Status Code :", r.status_code)

print(r.url)
print(r.text)

f = open("./page.html", "w+")
f.write(r.text)
