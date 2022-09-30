#Web scrapping para obter informações das músicas

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome()

#Acesso ao site
driver.get('https://www.vagalume.com.br/supercombo/discografia/')

#Extração propriamente dita
content = driver.page_source
soup = BeautifulSoup(content)

#Obtenção das músicas
name_musics = soup.find_all('a', href = True, attrs={'class':'nameMusic'})
musics_clear = []

for b1 in name_musics:
    b1 = b1.string.extract()
    musics_clear.append(b1)

#Obtenção das letras das músicas
lyrics = []
lyrics_hrefs = soup.find_all('a', href = True, attrs = {'class': 'nameMusic'})
links = []
for i in lyrics_hrefs:
    i = i.get('href')
    links.append(i)
#print(links)
for a in links:
    concat_link = 'https://www.vagalume.com.br' + a
    print(concat_link)
    driver.get(concat_link)
    content = driver.page_source
    time.sleep(1)
    soup = BeautifulSoup(content)
    music_lyric = soup.find_all('div', attrs ={'id':'lyrics'}) 
    
    lyric_clear = []
    
    for a1 in music_lyric:
        a1 = a1.get_text(" ", strip=True)
        lyric_clear.append(a1)
    
    lyrics.append(lyric_clear)    #print(musics_clear)
    
print(lyrics)

time = [166,201]
popularity =[681149,542702]
# driver.quit()