from bs4 import BeautifulSoup
import requests

search = input("Enter Search term:")
param = {"q": search}
r = requests.get("http://www.bing.com/search", param)

soap = BeautifulSoup(r.text, features="lxml")
print(soap.prettify())
