#!/user/bin/env python3
#http://2.python-requests.org/en/master/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup

#url = "https://www.humblebundle.com/books/cloud-computing-books"
url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
sections = soup.find_all("div", class_="section")
for section in sections[0]:
    print(section.text.strip())
# Bundle Tiers
# twos