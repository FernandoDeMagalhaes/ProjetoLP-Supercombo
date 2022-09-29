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
for a in soup.find_all('div', attrs={'class':'topLetrasWrapper'}):
    name_album = a.find('h3', attrs={'class':'albumTitle'}).get_text(strip=True)
    albums.append(name_album)

for b in soup.find_all('ol', attrs = {'id':'topMusicList'}):
    name_musics = b.find_all('a', href = True, attrs={'class':'nameMusic'})
    musics.append(name_musics)

for c in soup.find_all('div', attrs = {'class': 'cardAlbumInfos'}): 
    year = c.find('p', attrs={'class':'albumYear'}).get_text(strip=True)
    yearlaunching.append(year)

print(albums, "a")  
print(musics, "a")
print(yearlaunching, "a")    

df = pd.DataFrame({'Album': albums, 'Music': musics, 'Year': yearlaunching})
df.to_csv('supercombo.csv', index=False, encoding='utf-8')    