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
driver.get('https://www.vagalume.com.br/supercombo/discografia/')

#Extração propriamente dita
content = driver.page_source
soup = BeautifulSoup(content)

#Extrai o nome dos álbums e cria uma lista com eles
for a in soup.find_all('div', attrs={'class':'topLetrasWrapper'}):
    name_album = a.find('h3', attrs={'class':'albumTitle'}).get_text(strip=True)
    albums.append(name_album)

#Extrai o nome das músicas e cria uma lista de listas com elas
for b in soup.find_all('ol', attrs = {'id':'topMusicList'}):
    musics_clear = []
    name_musics = b.find_all('a', href = True, attrs={'class':'nameMusic'})
    
    for b1 in name_musics:
        b1 = b1.string.extract()
        musics_clear.append(b1)
        
    musics.append(musics_clear)

#Extrai o ano dos álbums e cria uma lista com eles
for c in soup.find_all('div', attrs = {'class': 'cardAlbumInfos'}): 
    year = c.find('p', attrs={'class':'albumYear'}).get_text(strip=True)
    yearlaunching.append(year)   

#Criação do DataFrame propriamente dito 
df = pd.DataFrame({'Album': albums, 'Music': musics, 'Year': yearlaunching})
df.to_csv('supercombo.csv', index=False, encoding='utf-8')    