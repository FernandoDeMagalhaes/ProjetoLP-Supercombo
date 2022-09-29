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
    
    musics_album = []
    
    name_album = a.find('h3', attrs={'class':'albumTitle'}).get_text(strip=True)
    for b in soup.find_all('div', attrs = {'class': 'lineColLeft'}): 
        name_musics = b.find('a', href = True, attrs={'class':'nameMusic'}).get_text(strip=True)
        musics_album.append(name_musics)
    # year = a.find('p', attrs={'class':'AlbumYear'}).get_text(strip=True)
    musics.append(musics_album)
    albums.append(name_album)
    
    # yearlaunching.append(year)
    # print(name_album)
# print(yearlaunching, "a")
print(albums, "a")  
print(musics, "a")
# print(yearlaunching, "a")    

# df = pd.DataFrame({'Album': albums, 'Music': musics, 'Year': yearlaunching})
# df.to_csv('supercombo.csv', index=False, encoding='utf-8')    