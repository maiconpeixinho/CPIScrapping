
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

for link in links:
    print("Downloading file: %s.pdf" % (link["name"]))
    r = requests.get(link["link"], stream = True)
    with open("%s.%s" % (link["name"],"pdf"),"wb") as pdf:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)