
from bs4 import BeautifulSoup

import os
import requests
import urllib

html = requests.get("https://legis.senado.leg.br/comissoes/docsRecCPI?codcol=2441").content

soup = BeautifulSoup(html, 'html.parser')

links = []

for table in soup.find_all("table", class_="table"):
    for anchor in table.find_all('a'):
        links.append({"name":anchor.contents[0], "link":anchor['href']})

print(links[0])

r = requests.get(links[0]["link"], stream = True)

with open("%s.%s" % (links[0]["name"],"pdf"),"wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
         # writing one chunk at a time to pdf file
         if chunk:
             pdf.write(chunk) 