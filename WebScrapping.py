import requests
from bs4 import BeautifulSoup

url ="https://www.elmundo.es"
r = requests.get(url)

r_html = r.text

# print(r_html)

soup = BeautifulSoup(r_html,features="html.parser")

title = soup.find_all("a")

for link in title:
    print(link.get('href'))


