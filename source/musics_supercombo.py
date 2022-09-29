#Web scrapping para obter informações das músicas

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

#Acesso ao site
driver.get('https://www.vagalume.com.br/supercombo/discografia/')

#Extração propriamente dita
content = driver.page_source
soup = BeautifulSoup(content)

name_musics = soup.find_all('a', href = True, attrs={'class':'nameMusic'})
musics_clear = []

for b1 in name_musics:
    b1 = b1.string.extract()
    musics_clear.append(b1)

print(musics_clear)