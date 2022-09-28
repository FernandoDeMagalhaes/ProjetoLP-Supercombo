#Web scrapping para extração dos dados a partir do HTML
#Fontes: Vagalume e Youtube

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

albums = [] #Consegue o nome dos álbuns para a música
musics = [] #Consegue o nome das músicas para os álbuns
yearlaunching = [] #Consegue o ano de lançamento de certo álbum

#Acesso ao site
driver.get("https://www.vagalume.com.br/supercombo/discografia/")

#Extração propriamente dita
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'letrasWrapper col1-2'}):
    name_album = a.find('h3', attrs={'class':'albumTitle'})
    name_musics = a.find('div', attrs={'class':'nameMusic'})
    year = a.find('p', attrs={'class':'AlbumYear'})
    albums.append(name_album.text)
    musics.append(name_musics.text)
    yearlaunching.append(year.text)
print(yearlaunching, "a")    
df = pd.DataFrame({'Album': albums, 'Music': musics, 'Year': yearlaunching})
df.to_csv('supercombo.csv', index=False, encoding='utf-8')    