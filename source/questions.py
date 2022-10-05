import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import math
import sys

# Função pra tirar texto entre parênteses
def ignorar_caracteres_cercados(texto, char_abertura, char_fechamento):
    profundidade = 0
    novo_texto = ''

    for c in texto:
        if c == char_abertura:
            profundidade += 1
        elif c == char_fechamento:
            profundidade -= 1
            if profundidade < 0:
                raise Exception('Cercamento não balanceado')
        elif profundidade == 0:
            novo_texto += c

    if profundidade > 0:
        raise Exception('Cercamento não balanceado')

    return novo_texto

#Leitura de arquivo
try:
    df1 = pd.read_csv('..\\dataframes\\supercombo.csv')
    df2 = pd.read_csv('..\\dataframes\\supercombo2.csv')
except FileNotFoundError as fnfe:
    print(dir(fnfe))
    print("Arquivo não existe!", fnfe)
    sys.exit()
else:
    print("Nenhum erro ocorreu, arquivo encontrado!")


# CONJUNTO DE PERGUNTAS 1

#mais longas e curtas por album:

musicas = df2['Music']
albuns = []
duracao = []

m1 = 0
for i in musicas:
    n1 = 0
    for j in df1['Music']:
        if i in j:
            albuns.append(df1['Album'][n1])
        n1 += 1
    duracao.append(df2['Time'][m1])
    m1 += 1

df_dur_album = pd.DataFrame({'Album': albuns, 'Musica': musicas, 'Duração': duracao})

temposList = []

n1 = 0
for i in df1['Album']:
    tempo = []
    m1 = 0
    for j in df2['Music']:
        if (i == df_dur_album['Album'][m1]):
            tempo.append(df_dur_album['Duração'][m1])
        m1 += 1
    
    temposList.append(tempo)
    n1 += 1

musicList = []

n1 = 0
for i in df1['Album']:
    m1 = 0
    music = []
    for j in df2['Music']:
        if (i == df_dur_album['Album'][m1]):
            music.append(j)
        m1 += 1

    musicList.append(music)
    n1 += 1
    
n2 = 0
for i in df1['Album']:
    df_tempo_album = pd.DataFrame({"Música": musicList[n2], "Tempo": temposList[n2]})
    
    print("Album: ", i, "\n")
    print("Mais longas: \n", df_tempo_album.sort_values(by = 'Tempo', ascending = False).head(3), "\n", sep="")
    print("Mais curtas: \n", df_tempo_album.sort_values(by = 'Tempo', ascending = True).head(3), sep="")
    print("\n\n")
    
    #Média do tempo das músicas por álbum:
    print("Média de tempo de música por álbum: ",round(df_tempo_album['Tempo'].mean(),2),"\n \n")
    
    n2 += 1


print("----" * 10)

# Mais ouvidas e menos ouvidas por álbum:

visualisacoes = []
m1 = 0
for i in musicas:
    visualisacoes.append(df2['Views'][m1])
    m1 += 1

df_viw_album = pd.DataFrame({'Album': albuns, 'Musica': musicas, 'Visualisações': visualisacoes})

viwList = []

n1 = 0
for i in df1['Album']:
    viw = []
    m1 = 0
    for j in df2['Music']:
        if (i == df_viw_album['Album'][m1]):
            viw.append(df_viw_album['Visualisações'][m1])
        m1 += 1
    viwList.append(viw)   
    n1 += 1

n1 = 0
for i in df1['Album']:
    m1 = 0
    music = []
    for j in df2['Music']:
        if (i == df_dur_album['Album'][m1]):
            music.append(j)
        m1 += 1

    musicList.append(music)
    n1 += 1
    
n2 = 0
for i in df1['Album']:
    df_r_viw_album = pd.DataFrame({"Música": musicList[n2], "Visualizações": viwList[n2]})
    
    print("Album: ", i, "\n")
    print("Mais vistas: \n", df_r_viw_album.sort_values(by = 'Visualizações', ascending = False).head(3), "\n", sep="")
    print("Menos vistas: \n", df_r_viw_album.sort_values(by = 'Visualizações', ascending = True).head(3), sep="")
    print("\n\n")
    
    n2 += 1

print("----" * 10)

# Mais longa e mais curta de todas

n3 = 0
for i in df_dur_album['Duração']:
    if i == max(df_dur_album['Duração']):
        print("Maior Música: ", df_dur_album['Musica'][n3])
    if i == min(df_dur_album['Duração']):
        print("Menor Música: ", df_dur_album['Musica'][n3])
    n3 += 1
    
print("\n")

print("----" * 10)


# Mais vista e menos vista de todas

n4 = 0
for i in df_viw_album['Visualisações']:
    if i == max(df_viw_album['Visualisações']):
        print("Mais Vista: ", df_viw_album['Musica'][n4])
    if i == min(df_viw_album['Visualisações']):
        print("Menos Vista: ", df_viw_album['Musica'][n4])
    n4 += 1

print("\n")

print("----" * 10)

# Album mais premiado

n5 = 0
for i in df1['Awards']:
    if i == max(df1['Awards']):
        print("Mais premiado: ", df1['Album'][n5])
    n5 += 1

print("\n")

print("----" * 10)

# Existe relação entre a duração e a popularidade?

mediaViw = df_viw_album['Visualisações'].mean()
desvpadViw = df_viw_album['Visualisações'].std()

mediaTempo = df_dur_album['Duração'].mean()
desvpadTempo = df_dur_album['Duração'].std()

somatorio_xy = 0
somatorio_x = 0
somatorio_y = 0

n4 = 0
for i in df_dur_album['Album']:
    soma1 = df_viw_album['Visualisações'][n4] - mediaViw
    soma2 = df_dur_album['Duração'][n4] - mediaTempo
    soma3 = soma1 * soma2
    
    somatorio_xy += soma3
    somatorio_x += (soma1 ** 2)
    somatorio_y += (soma2 ** 2)
    n4 += 1

r = somatorio_xy / math.sqrt(somatorio_x * somatorio_y)
    
print("O coeficiente de relação é: ", r , " Portanto não são relacionados \n")

print("----" * 10)

# CONJUNTO DE PERGUNTAS 2

# Palavras mais repetidas nos titulos dos albums

stringclear = []

for i in df1['Album']:
    string = i
    remove = "[];:!?.,'"
    for j in range(len(remove)):
        string = string.replace(remove[j],"")
    stringclear.append(string.upper())

bigstring = ""

for i in stringclear:
    bigstring = bigstring + " " + i

palavras = bigstring.split()

uniqWord = []
for i in palavras:
    if i not in uniqWord:
        uniqWord.append(i)

contagem = []
for i in uniqWord:
    contagem.append(bigstring.count(i))

df_contagem_album = pd.DataFrame({"Palavra": uniqWord, "Contagem": contagem})

print(df_contagem_album.sort_values(by = 'Contagem', ascending = False).head(3))

print("\n")

print("----" * 10)

# Palavras mais repetidas nos titulos da músicas

stringclear = []

for i in df2['Music']:
    string = i
    remove = "[];:!?.,'"
    for j in range(len(remove)):
        string = string.replace(remove[j],"")
    stringclear.append(string.upper())

bigstring = ""

for i in stringclear:
    bigstring = bigstring + " " + i

bigstring = ignorar_caracteres_cercados(bigstring, '(', ')')

palavras = bigstring.split()

uniqWord = []
for i in palavras:
    if i not in uniqWord:
        uniqWord.append(i)

remover = ['A','O','E','DA','DE','EU','AS','SE','DO','NA']

for i in remover:
    try:
        uniqWord.remove(i)
    except:
        pass

contagem = []
for i in uniqWord:
    contagem.append(bigstring.count(i))

df_contagem_album = pd.DataFrame({"Palavra": uniqWord, "Contagem": contagem})

print("Número \n", df_contagem_album.sort_values(by = 'Contagem', ascending = False).head(5))

print("\n")

print("----" * 10)

d = {}
for a, x in df_contagem_album.values:
    d[a] = x

wordcloud_titulo_album = WordCloud(
                                  background_color="black",
                                  width=1600, height=800).generate(" ".join(palavras))
wordcloud_titulo_album.generate_from_frequencies(frequencies=d)
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud_titulo_album, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud_titulo_album);
wordcloud_titulo_album.to_file("..\\images\\palavras_titulos_albuns.png")


# Palavras mais comuns nas letras em toda a discografia

stringclear = []

for i in df2['Lyrics']:
    string = i
    remove = "[];:!?.,'-"
    for j in range(len(remove)):
        string = string.replace(remove[j],"")
    stringclear.append(string.upper())

bigstring = ""

for i in stringclear:
    bigstring = bigstring + " " + i

bigstring = bigstring.replace("("," ")
bigstring = bigstring.replace(")"," ")

palavras = bigstring.split()

uniqWord = []
for i in palavras:
    if i not in uniqWord:
        uniqWord.append(i)
        
remover = ['A','E','O','DE','SE','QUE','EU','TE','DO','EM','ME','TA','OS','AS',
           'É','NÃO','VO','TO','DA','SO','EI','AI','IR','PRA','OU','NO','UM','CÊ',
           'VOCÊ','NA','HA','IA','COM','VI','Ó','SER','SEM','CON','SI','TU','MEU',
           'TEM','SÓ','OI','LI','AA','DEI','VER','VAI','PAR','POR','MAIS','FAZ','PRO',
           'NOS','AH','TER','VOU','ERA','SEI','SOU','DOS','ESTA','DAR','MAS','DEIXA','ESSE',
           'ELA','QUER','COMO','QUANDO','MINHA','QUEM']

for i in remover:
    try:
        uniqWord.remove(i)
        while True:
            palavras.remove(i)
    except:
        pass


contagem = []
for i in uniqWord:
    contagem.append(bigstring.count(i))

df_contagem_letra = pd.DataFrame({"Palavra": uniqWord, "Contagem": contagem})

print(df_contagem_letra.sort_values(by = 'Contagem', ascending = False).head(10))

print("\n")

print("----" * 10)

#Montagem da wordcloud de palvras de toda a discografia

d = {}
for a, x in df_contagem_letra.values:
    d[a] = x

wordcloud_discografia = WordCloud(
                                  background_color="black",
                                  width=1600, height=800).generate(" ".join(palavras))
wordcloud_discografia.generate_from_frequencies(frequencies=d)
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud_discografia, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud_discografia);
wordcloud_discografia.to_file("..\\images\\palavras_discografia.png")

# Palavras mais comuns nas letras por album

musicas = df2['Music']
albuns = []
letras = []

m1 = 0
for i in musicas:
    n1 = 0
    for j in df1['Music']:
        if i in j:
            albuns.append(df1['Album'][n1])
        n1 += 1
    letras.append(df2['Lyrics'][m1])
    m1 += 1
    
df_lyric_album = pd.DataFrame({'Album': albuns, 'Musica': musicas, 'Letras': letras})

liricList = []

for i in df1['Album']:
    liric = []
    m7 = 0
    for j in df2['Lyrics']:
        if (i == df_lyric_album['Album'][m7]):
            liric.append(df_lyric_album['Letras'][m7])
        m7 += 1
    liricList.append(liric)

stringclearList = []

for j in liricList:
    stringclear = []
    for i in j:
        string = i
        remove = "[];:!?.,'-"
        for k in range(len(remove)):
            string = string.replace(remove[k],"")
        stringclear.append(string.upper())
    
    stringclearList.append(stringclear)

contagemList = []
uniqWordList = []
palavrasList = []

for i in stringclearList:
    bigstring = ""

    for j in i:
        bigstring = bigstring + " " + j

    bigstring = bigstring.replace("("," ")
    bigstring = bigstring.replace(")"," ")

    palavras = bigstring.split()
    
    uniqWord = []
    for k in palavras:
        if k not in uniqWord:
            uniqWord.append(k)
    
    remover = ['A','E','O','DE','SE','QUE','EU','TE','DO','EM','ME','TA','OS','AS',
               'É','NÃO','VO','TO','DA','SO','EI','AI','IR','PRA','OU','NO','UM','CÊ',
               'VOCÊ','NA','HA','IA','COM','VI','Ó','SER','SEM','CON','AR','SI','TU','MEU',
               'TEM','SÓ','OI','LI','AA','DEI','VER','VAI','PAR','POR','MAIS','FAZ','PRO',
               'NOS','AH','TER','VOU','ERA','SEI','SOU','DOS','ESTA','DAR','MAS','DEIXA','ESSE',
               'ELA','QUER','COMO','QUANDO','MINHA','QUEM', 'OH', 'FOR', 'DEVE', 'TÁ', 'AÍ',
               'TÃO', 'AAAAA', 'MIM', 'WAAAA', 'OOO', 'UOOO', 'AAAAAH', 'JÁ']

    for i in remover:
        try:
            uniqWord.remove(i)
            while True:
                palavras.remove(i)
        except:
            pass
    
    uniqWordList.append(uniqWord)
    palavrasList.append(palavras)
            
    contagem = []
    for l in uniqWord:
        contagem.append(bigstring.count(l))
    
    contagemList.append(contagem)

n9 = 0
for i in df1['Album']:
    df_contagem_letra_album = pd.DataFrame({"Palavra": uniqWordList[n9], "Contagem": contagemList[n9]})
    print(i, "\n", df_contagem_letra_album.sort_values(by = 'Contagem', ascending = False).head(10),"\n")
    
    
    d = {}
    for a, x in df_contagem_letra_album.values:
        d[a] = x

    wordcloud_album = WordCloud(
                                      background_color="black",
                                      width=1600, height=800).generate(" ".join(palavrasList[n9]))
    wordcloud_album.generate_from_frequencies(frequencies=d)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud_album, interpolation='bilinear')
    ax.set_axis_off()
    plt.imshow(wordcloud_album);
    wordcloud_album.to_file("..\\images\\palavras_album_" + str(n9) + ".png") 
    
    n9 += 1

print("----" * 10)

# Palavras do titulo dos albuns como tema nas músicas

musicas = df2['Music']
albuns = []
letras = []

m1 = 0
for i in musicas:
    n1 = 0
    for j in df1['Music']:
        if i in j:
            albuns.append(df1['Album'][n1])
        n1 = n1+1
    letras.append(df2['Lyrics'][m1])
    m1 = m1 + 1
    
df_lyric_album = pd.DataFrame({'Album': albuns, 'Musica': musicas, 'Letras': letras})

liricList = []

for i in df1['Album']:
    liric = []
    m7 = 0
    for j in df2['Lyrics']:
        if (i == df_lyric_album['Album'][m7]):
            liric.append(df_lyric_album['Letras'][m7])
        m7 = m7+1
    liricList.append(liric)

stringclearList = []
albumclearList = []

for j in liricList:
    stringclear = []
    for i in j:
        string = i
        remove = "[];:!?.,'-"
        for k in range(len(remove)):
            string = string.replace(remove[k],"")
        stringclear.append(string.upper())
    
    stringclearList.append(stringclear)


albumclear = []
for j in df1['Album']:
    string = j
    remove = "[];:!?.,'-"
    for k in range(len(remove)):
        string = string.replace(remove[k],"")
    albumclear.append(string.upper())

uniqWordList = []

palavras1 = []

for i in stringclearList:
    bigstring1 = ""
    
    for j in i:
        bigstring1 = bigstring1 + " " + j

    bigstring1 = bigstring1.replace("("," ")
    bigstring1 = bigstring1.replace(")"," ")

    palavras = bigstring1.split()
    
    remover = ['A','E','O','DE','SE','QUE','EU','TE','DO','EM','ME','TA','OS','AS',
               'É','NÃO','VO','TO','DA','SO','EI','AI','IR','PRA','OU','NO','UM','CÊ',
               'VOCÊ','NA','HA','IA','COM','VI','Ó','SER','SEM','CON','SI','TU','MEU',
               'TEM','SÓ','OI','LI','AA','DEI','VER','VAI','PAR','POR','MAIS','FAZ','PRO',
               'NOS','AH','TER','VOU','ERA','SEI','SOU','DOS','ESTA','DAR','MAS','DEIXA','ESSE',
               'ELA','QUER','COMO','QUANDO','MINHA','QUEM', 'OH', 'FOR', 'DEVE', 'TÁ', 'AÍ',
               'TÃO', 'AAAAA', 'MIM', 'WAAAA', 'OOO', 'UOOO', 'AAAAAH', 'JÁ']

    for i in remover:
        try:
            while True:
                palavras.remove(i)
        except:
            pass
    
    palavras1.append(palavras)


palavras2 = []

for i in albumclear:

    i = i.replace("("," ")
    i = i.replace(")"," ")

    palavras2.append(i.split())

contagemList = []

n11 = 0
for i in palavras2:
    contagem = []
    for l in i:
        contagem.append(palavras1[n11].count(l))

    contagemList.append(contagem)
    n11 += 1


n12 = 0
for i in df1['Album']:
    df_titulo_album_letra = pd.DataFrame({"Palavra": palavras2[n12], "Contagem": contagemList[n12]})
    
    print(i, "\n")
    print(df_titulo_album_letra.sort_values(by = 'Contagem', ascending = False))
    print("\n")
    
    n12 = n12 + 1

print("----" * 10)

# Titulo das músicas são tema recorente nas letras?

stringclear1 = []
for j in df2['Music']:
    string = j
    remove = "[];:!?.,'-"
    for k in range(len(remove)):
        string = string.replace(remove[k],"")
    stringclear1.append(string.upper())

n13 = 0
for i in stringclear1:
    stringclear1[n13] = ignorar_caracteres_cercados(stringclear1[n13], '(', ')')
    
    stringclear1[n13] = stringclear1[n13].split()

    remover = ['A','O','E','DA','DE','EU','AS','SE','DO','NA']

    for j in remover:
        try:
            while True:
               stringclear1[n13].remove(j)
        except:
            pass
        
    n13 += 1
    
stringclear2 = []
for j in df2['Lyrics']:
    string = j
    remove = "[];:!?.,'-"
    for k in range(len(remove)):
        string = string.replace(remove[k],"")
    stringclear2.append(string.upper())


n14 = 0
for i in stringclear2:
    
    stringclear2[n14] = stringclear2[n14].replace("("," ")
    stringclear2[n14] = stringclear2[n14].replace(")"," ")
    
    stringclear2[n14] = stringclear2[n14].split()
    
    remover = ['A','E','O','DE','SE','QUE','EU','TE','DO','EM','ME','TA','OS','AS',
               'É','VO','TO','DA','SO','EI','AI','IR','PRA','OU','NO','UM','CÊ',
               'VOCÊ','NA','HA','IA','COM','VI','Ó','SER','SEM','CON','SI','TU','MEU',
               'TEM','SÓ','OI','LI','AA','DEI','VER','VAI','PAR','MAIS','FAZ','PRO',
               'NOS','AH','TER','VOU','ERA','SEI','SOU','DOS','ESTA','DAR','MAS','DEIXA','ESSE',
               'QUER','QUANDO','MINHA','QUEM', 'OH', 'FOR', 'DEVE', 'TÁ', 'AÍ',
               'TÃO', 'AAAAA', 'MIM', 'WAAAA', 'OOO', 'UOOO', 'AAAAAH', 'JÁ']

    for j in remover:
        try:
            while True:
                stringclear2[n14].remove(j)
        except:
            pass
    
    n14 += 1

contagemList = []

n11 = 0
for i in stringclear1:
    contagem = []
    for l in i:
        contagem.append(stringclear2[n11].count(l))

    contagemList.append(contagem)
    n11 += 1

n15 = 0
for i in df2['Music']:
    df_titulo_musica_letra = pd.DataFrame({"Palavra": stringclear1[n15], "Contagem": contagemList[n15]})
    
    print(i, "\n")
    print(df_titulo_musica_letra.sort_values(by = 'Contagem', ascending = False))
    print("\n")
    
    n15 = n15 + 1

print("----" * 10)

#Conjunto de perguntas 3 - A primeira pergunta está na parte anterior
#(Médias do tamanho das músicas por álbum)

#Média do tempo das músicas
print("Média do tempo das músicas na discografia: ", round(df2['Time'].mean(),2),'\n')

print("----" * 10)

#Gravadora mais comum, com número de vezes
recorders = df1['Recorders'].value_counts().sort_values(ascending = False).head(1)
print("Gravadora mais comum e número de vezes: \n ", recorders.to_string())

print("----" * 10)
