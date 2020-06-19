from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# Automation script which fetch URL from Amazon.in using Beautiful Soup.
# Url :- https://www.amazon.in/s?k=macbook&ref=nb_sb_noss
my_url = "https://en.wikipedia.org/wiki/Main_Page"
html = urlopen(my_url)
# print(html.read())
bs = BeautifulSoup(html, "html.parser")

links = bs.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("(/wiki/)([A-Za-z0-9_:()%])"))

for i in links:
    print(f"title of link : {i['title']}\nlink : {i['href']}\n")