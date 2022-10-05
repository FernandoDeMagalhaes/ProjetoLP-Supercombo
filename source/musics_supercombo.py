#Web scrapping para obter informações das músicas
import sys
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

for a in links:
    concat_link = 'https://www.vagalume.com.br' + a
    print(concat_link)
    try:
        driver.get(concat_link)
    except:
        print("Houve problema no acesso ao site: " + concat_link + ". Encerrando o programa." )
        sys.exit()
    content = driver.page_source
    time.sleep(1)
    soup = BeautifulSoup(content)
    music_lyric = soup.find_all('div', attrs ={'id':'lyrics'}) 
    
    lyric_clear = []
    
    for a1 in music_lyric:
        a1 = a1.get_text(" ", strip=True)
        lyric_clear.append(a1)
    
    lyrics.append(lyric_clear)    
    
#Tempo e popularidades(feitos à mão). Fonte: Youtube. O tempo está em segundos.
time = [166,201,188,227,189,201,233,163,208,192,205,223,
        235,231,245,202,219,214,201,193,215,197,128,219,
        217,161,251,225,204,202,221,243,191,257,90,203,
        212,213,223,215,234,218,240,216,234,200,268,233,
        273,258,210,212,220,229,266,197,259,194,234,260,
        342,205,223,252,317]
#Quantidade de visualizações em 30 de setembro de 2022.
popularity =[681149,542702,318115,444143,1030714,273518,1051068,499117,
             445999,715099,1155225,2227523,972071,1684821,4399634,630483,
             911346,852584,1842653,1020227,2478272,275182,497986,168812,
             47085674,619058,1361894,607591,1041412,739480,4221860,441348,
             558264,43836922,164407,759597,356612,529477,341182,1524142,
             565418,565256,587206,654659,384597,187744,186875,85078,374652,
             229419,226696,94461,54902,79694,66802,72093,299712,50162,160477,
             157501,169283,106524,174380,143512,150704]
#Encerrar a busca
driver.quit()

#Criação do dataframe
df = pd.DataFrame({'Music': musics_clear, 'Lyrics': lyrics, 'Time': time, 'Views': popularity})
df.to_csv('..\\dataframes\\supercombo2.csv', index=False, encoding='utf-8')