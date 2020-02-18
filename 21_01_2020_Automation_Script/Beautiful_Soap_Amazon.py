# Automation script which fetch URL from Amazon.in using Beautiful Soup.
# Url :- https://www.amazon.in/s?k=macbook&ref=nb_sb_noss

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

my_url = "https://www.amazon.in/s?k=macbook&ref=nb_sb_noss"
html = urlopen(my_url)
# print(html.read())
bs = BeautifulSoup(html, "html.parser")

# links = bs.find("div", {"id": "bodyContent"}).findAll("a")

containers = bs.findAll("div", {"class": "a-section a-spacing-medium"})
# for i in containers:
#     print(i)
print(len(containers))
# print(containers[0])
# container = containers[0]
# print(container.div)
