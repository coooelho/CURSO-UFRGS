import requests
import pandas as pd
import html.parser

from bs4 import BeautifulSoup
def getdata(url):
    r = requests.get(url)
    return r.text

htmldoc = getdata("https://g1.globo.com/politica/")
soup = BeautifulSoup(htmldoc, 'html.parser')
paragrafo = ''
for paragrafo in soup.find_all("Bolsonaro", "Lula"):
    print(paragrafo.get_text())

with open('lulaboso.txt', 'w') as arquivo:
    arquivo.write(paragrafo)