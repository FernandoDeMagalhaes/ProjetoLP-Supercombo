import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import math
import seaborn as sns

# Função pra tirar texto entre parênteses
def ignorar_caracteres_cercados(text, char_open, char_close):
    
    """
    Function used to remove text between parentheses from a string

    :param text: str
    :param char_open: str
    :param char_close: str
    
    :return str novo_texto:

    """
    
    prof = 0
    new_text = ''

    for c in text:
        if c == char_open:
            prof += 1
        elif c == char_close:
            prof -= 1
            if prof < 0:
                raise Exception('Cercamento não balanceado')
        elif prof == 0:
            new_text += c

    if prof > 0:
        raise Exception('Cercamento não balanceado')

    return new_text


# CONJUNTO DE PERGUNTAS 1

#mais longas e curtas por album:

def longa_curta_album(df1,df2):
    
    """
    Prints the 3 longest, 3 shortest, and average length of songs for each album on the console.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    musics = df2['Music']
    albuns = []
    duration = []
    
    m1 = 0
    for i in musics:
        n1 = 0
        for j in df1['Music']:
            if i in j:
                albuns.append(df1['Album'][n1])
            n1 += 1
        duration.append(df2['Time'][m1])
        m1 += 1
    
    df_time_album = pd.DataFrame({'Album': albuns, 'Musica': musics, 'Duração': duration})
    
    timesList = []

    for i in df1['Album']:
        time = []
        m2 = 0
        for j in df2['Music']:
            if (i == df_time_album['Album'][m2]):
                time.append(df_time_album['Duração'][m2])
            m2 += 1
        
        timesList.append(time)
    
    musicList = []
    
    for i in df1['Album']:
        m3 = 0
        music = []
        for j in df2['Music']:
            if (i == df_time_album['Album'][m3]):
                music.append(j)
            m3 += 1
    
        musicList.append(music)
        
    n2 = 0
    for i in df1['Album']:
        df_r_time_album = pd.DataFrame({"Música": musicList[n2], "Tempo": timesList[n2]})
        
        print("Album: ", i, "\n")
        print("Mais longas: \n", df_r_time_album.sort_values(by = 'Tempo', ascending = False).head(3), "\n", sep="")
        print("Mais curtas: \n", df_r_time_album.sort_values(by = 'Tempo', ascending = True).head(3), sep="")
        print("\n\n")
        
        #Média do tempo das músicas por álbum:
        print("Média de tempo de música por álbum: ",round(df_r_time_album['Tempo'].mean(),2),"\n \n")
    
        #Seaborn plot
        sns.barplot(x="Tempo", y="Música", data=df_r_time_album.sort_values(by = 'Tempo', ascending = False), color="b")
        # g.ax.axline(xy1=(10, 2), slope=.2, color="b", dashes=(5, 2))
        plt.savefig("..\\images\\time_album" + str(n2) + ".png", dpi = 300, bbox_inches = 'tight')
        
        n2 += 1
# Mais ouvidas e menos ouvidas por álbum:

def popular_inpopular_album(df1,df2):
    
    """
    Prints the 3 most popular and 3 least popular songs from each album on the console.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    musics = df2['Music']
    albuns = []
    viws = []
    
    m1 = 0
    for i in musics:
        viws.append(df2['Views'][m1])
        m1 += 1
    
    for i in musics:
        n1 = 0
        for j in df1['Music']:
            if i in j:
                albuns.append(df1['Album'][n1])
            n1 += 1

    df_viw_album = pd.DataFrame({'Album': albuns, 'Musica': musics, 'Visualisações': viws})
    
    viwList = []
    
    for i in df1['Album']:
        viw = []
        m2 = 0
        for j in df2['Music']:
            if (i == df_viw_album['Album'][m2]):
                viw.append(df_viw_album['Visualisações'][m2])
            m2 += 1
        viwList.append(viw)   

    musicList = []

    for i in df1['Album']:
        m3 = 0
        music = []
        for j in df2['Music']:
            if (i == df_viw_album['Album'][m3]):
                music.append(j)
            m3 += 1
    
        musicList.append(music)
        
    n2 = 0
    for i in df1['Album']:
        df_r_viw_album = pd.DataFrame({"Música": musicList[n2], "Visualizações": viwList[n2]})
        
        print("Album: ", i, "\n")
        print("Mais vistas: \n", df_r_viw_album.sort_values(by = 'Visualizações', ascending = False).head(3), "\n", sep="")
        print("Menos vistas: \n", df_r_viw_album.sort_values(by = 'Visualizações', ascending = True).head(3), sep="")
        print("\n\n")
        
        n2 += 1


# Mais longa e mais curta de todas

def longa_curta(df1,df2):
    
    """
    Prints the longest and shortest song in the entire discography on the console.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    musics = df2['Music']
    albuns = []
    duration = []
    
    m1 = 0
    for i in musics:
        n1 = 0
        for j in df1['Music']:
            if i in j:
                albuns.append(df1['Album'][n1])
            n1 += 1
        duration.append(df2['Time'][m1])
        m1 += 1
    
    df_dur_album = pd.DataFrame({'Album': albuns, 'Musica': musics, 'Duração': duration})
    
    n2 = 0
    for i in df_dur_album['Duração']:
        if i == max(df_dur_album['Duração']):
            print("Maior Música: ", df_dur_album['Musica'][n2])
        if i == min(df_dur_album['Duração']):
            print("Menor Música: ", df_dur_album['Musica'][n2])
        n2 += 1
        
    print("\n")


# Mais vista e menos vista de todas

def popular_inpopular(df1,df2):
    
    """
    Prints on the console the most popular and least popular song of the entire discography.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    musics = df2['Music']
    albuns = []
    viws = []

    m1 = 0
    for i in musics:
        viws.append(df2['Views'][m1])
        m1 += 1
    
    for i in musics:
        n1 = 0
        for j in df1['Music']:
            if i in j:
                albuns.append(df1['Album'][n1])
            n1 += 1

    df_viw_album = pd.DataFrame({'Album': albuns, 'Musica': musics, 'Visualisações': viws})

    n2 = 0
    for i in df_viw_album['Visualisações']:
        if i == max(df_viw_album['Visualisações']):
            print("Mais Vista: ", df_viw_album['Musica'][n2])
        if i == min(df_viw_album['Visualisações']):
            print("Menos Vista: ", df_viw_album['Musica'][n2])
        n2 += 1

    print("\n")


# Album mais premiado

def premiados(df1,df2):
    
    """
    Prints the band's most awarded album on the console.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    n = 0
    for i in df1['Awards']:
        if i == max(df1['Awards']):
            print("Mais premiado: ", df1['Album'][n])
        n += 1
    
    print("\n")


# Existe relação entre a duração e a popularidade?

def relacao_tempo_popularidade(df1,df2):
    
    """
    Prints on the console the Linear Correlation Coefficient between the size of the song and its popularity and creates a seaborn plot with the data.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    musics = df2['Music']
    albuns = []
    times = []
    viws = []
    
    m1 = 0
    for i in musics:
        n1 = 0
        for j in df1['Music']:
            if i in j:
                albuns.append(df1['Album'][n1])
            n1 += 1
        times.append(df2['Time'][m1])
        m1 += 1
        
    m2 = 0
    for i in musics:
        viws.append(df2['Views'][m2])
        m2 += 1
    
    df_dur_viw_album = pd.DataFrame({'Album': albuns, 'Musica': musics, 'Duração': times, 'Visualisações': viws})
    
    viwMean = df_dur_viw_album['Visualisações'].mean()
    timeMean = df_dur_viw_album['Duração'].mean()
    
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    
    n2 = 0
    for i in df_dur_viw_album['Album']:
        soma1 = df_dur_viw_album['Visualisações'][n2] - viwMean
        soma2 = df_dur_viw_album['Duração'][n2] - timeMean
        soma3 = soma1 * soma2
        
        sum_xy += soma3
        sum_x += (soma1 ** 2)
        sum_y += (soma2 ** 2)
        n2 += 1
    
    r = sum_xy / math.sqrt(sum_x * sum_y)
        
    print("O coeficiente de relação é: ", r , " Portanto não são relacionados \n")
    
    #Seaborn plot
    g = sns.lmplot(data=df1, x="Time", y="Views")
    g.ax.axline(xy1=(10, 2), slope=.2, color="b", dashes=(5, 2))
    plt.savefig("..\\images\\mean_time.png",dpi = 300, bbox_inches = 'tight')

    
# CONJUNTO DE PERGUNTAS 2

# Palavras mais repetidas nos titulos dos albums

def palavras_titulos_albuns(df1,df2):
    
    """
    Prints on the console the most common words in album titles.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
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
    
    words = bigstring.split()
    
    uniqWord = []
    for i in words:
        if i not in uniqWord:
            uniqWord.append(i)
    
    score = []
    for i in uniqWord:
        score.append(bigstring.count(i))
    
    df_score_album = pd.DataFrame({"Palavra": uniqWord, "Contagem": score})
    
    print(df_score_album.sort_values(by = 'Contagem', ascending = False).head(3))
    
    print("\n")


# Palavras mais repetidas nos titulos da músicas

def palavras_titulos_musicas(df1,df2):
    
    """
    Prints on the console the most common words in song titles and creates the wordcloud.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
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
    
    words = bigstring.split()
    
    uniqWord = []
    
    for i in words:
        if i not in uniqWord:
            uniqWord.append(i)
    
    removeWords = ['A','O','E','DA','DE','EU','AS','SE','DO','NA']
    
    for i in removeWords:
        try:
            uniqWord.remove(i)
        except:
            pass
    
    score = []
    
    for i in uniqWord:
        score.append(bigstring.count(i))
    
    df_score_album = pd.DataFrame({"Palavra": uniqWord, "Contagem": score})
    
    print("Número \n", df_score_album.sort_values(by = 'Contagem', ascending = False).head(5))
    
    print("\n")

    d = {}
    for a, x in df_score_album.values:
        d[a] = x
    
    wordcloud_titulo_album = WordCloud(background_color="black", width=1600, height=800).generate(" ".join(words))
    wordcloud_titulo_album.generate_from_frequencies(frequencies=d)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud_titulo_album, interpolation='bilinear')
    ax.set_axis_off()
    plt.imshow(wordcloud_titulo_album);
    wordcloud_titulo_album.to_file("..\\images\\palavras_titulos_albuns.png")


# Palavras mais comuns nas letras em toda a discografia

def palavras_letras(df1,df2):
    
    """
    Prints on the console the most common words in the lyrics of the songs and creates the wordcloud.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
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
    
    words = bigstring.split()
    
    uniqWord = []
    for i in words:
        if i not in uniqWord:
            uniqWord.append(i)
            
    removeWords = ['A','E','O','DE','SE','QUE','EU','TE','DO','EM','ME','TA','OS','AS',
                   'É','NÃO','VO','TO','DA','SO','EI','AI','IR','PRA','OU','NO','UM','CÊ',
                   'VOCÊ','NA','HA','IA','COM','VI','Ó','SER','SEM','CON','SI','TU','MEU',
                   'TEM','SÓ','OI','LI','AA','DEI','VER','VAI','PAR','POR','MAIS','FAZ','PRO',
                   'NOS','AH','TER','VOU','ERA','SEI','SOU','DOS','ESTA','DAR','MAS','DEIXA','ESSE',
                   'ELA','QUER','COMO','QUANDO','MINHA','QUEM','AR']
    
    for i in removeWords:
        try:
            uniqWord.remove(i)
            while True:
                words.remove(i)
        except:
            pass
    
    score = []
    for i in uniqWord:
        score.append(bigstring.count(i))
    
    df_score_letra = pd.DataFrame({"Palavra": uniqWord, "Contagem": score})
    
    print(df_score_letra.sort_values(by = 'Contagem', ascending = False).head(10))
    
    print("\n")

    #Montagem da wordcloud de palvras de toda a discografia
    
    d = {}
    for a, x in df_score_letra.values:
        d[a] = x
    
    wordcloud_discografia = WordCloud(background_color="black", width=1600, height=800).generate(" ".join(words))
    wordcloud_discografia.generate_from_frequencies(frequencies=d)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud_discografia, interpolation='bilinear')
    ax.set_axis_off()
    plt.imshow(wordcloud_discografia);
    wordcloud_discografia.to_file("..\\images\\palavras_discografia.png")


# Palavras mais comuns nas letras por album

def palavras_letras_album(df1,df2):
    
    """    
    Prints on the console the most common words in the lyrics of the songs by album and creates the wordcloud.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    musics = df2['Music']
    albuns = []
    lirics = []
    
    m1 = 0
    for i in musics:
        n1 = 0
        for j in df1['Music']:
            if i in j:
                albuns.append(df1['Album'][n1])
            n1 += 1
        lirics.append(df2['Lyrics'][m1])
        m1 += 1
        
    df_lyric_album = pd.DataFrame({'Album': albuns, 'Musica': musics, 'Letras': lirics})
    
    liricList = []
    
    for i in df1['Album']:
        liric = []
        m2 = 0
        for j in df2['Lyrics']:
            if (i == df_lyric_album['Album'][m2]):
                liric.append(df_lyric_album['Letras'][m2])
            m2 += 1
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
    
    scoreList = []
    uniqWordList = []
    wordsList = []
    
    for i in stringclearList:
        bigstring = ""
    
        for j in i:
            bigstring = bigstring + " " + j
    
        bigstring = bigstring.replace("("," ")
        bigstring = bigstring.replace(")"," ")
    
        words = bigstring.split()
        
        uniqWord = []
        
        for k in words:
            if k not in uniqWord:
                uniqWord.append(k)
        
        removeWords = ['A','E','O','DE','SE','QUE','EU','TE','DO','EM','ME','TA','OS','AS',
                       'É','NÃO','VO','TO','DA','SO','EI','AI','IR','PRA','OU','NO','UM','CÊ',
                       'VOCÊ','NA','HA','IA','COM','VI','Ó','SER','SEM','CON','AR','SI','TU','MEU',
                       'TEM','SÓ','OI','LI','AA','DEI','VER','VAI','PAR','POR','MAIS','FAZ','PRO',
                       'NOS','AH','TER','VOU','ERA','SEI','SOU','DOS','ESTA','DAR','MAS','DEIXA','ESSE',
                       'ELA','QUER','COMO','QUANDO','MINHA','QUEM', 'OH', 'FOR', 'DEVE', 'TÁ', 'AÍ',
                       'TÃO', 'AAAAA', 'MIM', 'WAAAA', 'OOO', 'UOOO', 'AAAAAH', 'JÁ']
    
        for i in removeWords:
            try:
                uniqWord.remove(i)
                while True:
                    words.remove(i)
            except:
                pass
        
        uniqWordList.append(uniqWord)
        wordsList.append(words)
                
        score = []
        
        for l in uniqWord:
            score.append(bigstring.count(l))
        
        scoreList.append(score)
    
    n2 = 0
    for i in df1['Album']:
        df_score_lyric_album = pd.DataFrame({"Palavra": uniqWordList[n2], "Contagem": scoreList[n2]})
        print(i, "\n", df_score_lyric_album.sort_values(by = 'Contagem', ascending = False).head(10),"\n")
        
        
        d = {}
        for a, x in df_score_lyric_album.values:
            d[a] = x
    
        wordcloud_album = WordCloud(background_color="black", width=1600, height=800).generate(" ".join(wordsList[n2]))
        wordcloud_album.generate_from_frequencies(frequencies=d)
        fig, ax = plt.subplots(figsize=(10,6))
        ax.imshow(wordcloud_album, interpolation='bilinear')
        ax.set_axis_off()
        plt.imshow(wordcloud_album);
        wordcloud_album.to_file("..\\images\\palavras_album_" + str(n2) + ".png") 
        
        n2 += 1


# Palavras do titulo dos albuns como tema nas músicas

def palavras_album_tema(df1,df2):
    
    """    
    Prints in the console the occurrences of the words of the album title in the lyrics of that album.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    musics = df2['Music']
    albuns = []
    lyrics = []
    
    m1 = 0
    for i in musics:
        n1 = 0
        for j in df1['Music']:
            if i in j:
                albuns.append(df1['Album'][n1])
            n1 += 1
        lyrics.append(df2['Lyrics'][m1])
        m1 += 1
        
    df_lyric_album = pd.DataFrame({'Album': albuns, 'Musica': musics, 'Letras': lyrics})
    
    liricList = []
    
    for i in df1['Album']:
        liric = []
        m2 = 0
        for j in df2['Lyrics']:
            if (i == df_lyric_album['Album'][m2]):
                liric.append(df_lyric_album['Letras'][m2])
            m2 += 1
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
    
    albumclear = []
    
    for j in df1['Album']:
        string = j
        remove = "[];:!?.,'-"
        for k in range(len(remove)):
            string = string.replace(remove[k],"")
        albumclear.append(string.upper())

    wordsList1 = []
    
    for i in stringclearList:
        bigstring1 = ""
        
        for j in i:
            bigstring1 = bigstring1 + " " + j
    
        bigstring1 = bigstring1.replace("("," ")
        bigstring1 = bigstring1.replace(")"," ")
    
        words = bigstring1.split()
        
        removeWords = ['A','E','O','DE','SE','QUE','EU','TE','DO','EM','ME','TA','OS','AS',
                       'É','NÃO','VO','TO','DA','SO','EI','AI','IR','PRA','OU','NO','UM','CÊ',
                       'VOCÊ','NA','HA','IA','COM','VI','Ó','SER','SEM','CON','SI','TU','MEU',
                       'TEM','SÓ','OI','LI','AA','DEI','VER','VAI','PAR','POR','MAIS','FAZ','PRO',
                       'NOS','AH','TER','VOU','ERA','SEI','SOU','DOS','ESTA','DAR','MAS','DEIXA','ESSE',
                       'ELA','QUER','COMO','QUANDO','MINHA','QUEM', 'OH', 'FOR', 'DEVE', 'TÁ', 'AÍ',
                       'TÃO', 'AAAAA', 'MIM', 'WAAAA', 'OOO', 'UOOO', 'AAAAAH', 'JÁ']
    
        for i in removeWords:
            try:
                while True:
                    words.remove(i)
            except:
                pass
        
        wordsList1.append(words)
    
    wordsList2 = []
    
    for i in albumclear:
    
        i = i.replace("("," ")
        i = i.replace(")"," ")
    
        wordsList2.append(i.split())
    
    scoreList = []
    
    n2 = 0
    for i in wordsList2:
        score = []
        for l in i:
            score.append(wordsList1[n2].count(l))
    
        scoreList.append(score)
        n2 += 1
    
    n3 = 0
    for i in df1['Album']:
        df_title_album_lyric = pd.DataFrame({"Palavra": wordsList2[n3], "Contagem": scoreList[n3]})
        
        print(i, "\n")
        print(df_title_album_lyric.sort_values(by = 'Contagem', ascending = False))
        print("\n")
        
        n3 = n3 + 1
    
    print("Analisando os dataframes acima, percebe-se que o título do álbum não é tema recorrente, com exceção para o álbum 'Rogério'.")


# Titulo das músicas são tema recorente nas letras?

def palavras_musica_tema(df1,df2):
    
    """    
    Prints on the console the occurrences of the words of the song title in the lyrics of the same.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    stringclear1 = []
    for j in df2['Music']:
        string = j
        remove = "[];:!?.,'-"
        for k in range(len(remove)):
            string = string.replace(remove[k],"")
        stringclear1.append(string.upper())
    
    n1 = 0
    for i in stringclear1:
        stringclear1[n1] = ignorar_caracteres_cercados(stringclear1[n1], '(', ')')
        
        stringclear1[n1] = stringclear1[n1].split()
    
        removeWords1 = ['A','O','E','DA','DE','AS','DO','NA']
    
        for j in removeWords1:
            try:
                while True:
                    stringclear1[n1].remove(j)
            except:
                pass
            
        n1 += 1
        
    stringclear2 = []
    for j in df2['Lyrics']:
        string = j
        remove = "[];:!?.,'-"
        for k in range(len(remove)):
            string = string.replace(remove[k],"")
        stringclear2.append(string.upper())
    
    n2 = 0
    for i in stringclear2:
        
        stringclear2[n2] = stringclear2[n2].replace("("," ")
        stringclear2[n2] = stringclear2[n2].replace(")"," ")
        
        stringclear2[n2] = stringclear2[n2].split()
        
        removeWords2 = ['A','E','O','DE','QUE','TE','DO','EM','ME','TA','OS','AS',
                        'É','VO','TO','DA','SO','EI','AI','IR','PRA','OU','NO','UM','CÊ',
                        'VOCÊ','NA','HA','IA','COM','VI','Ó','SER','SEM','CON','SI','TU','MEU',
                        'TEM','SÓ','OI','LI','AA','DEI','VER','VAI','PAR','MAIS','FAZ','PRO',
                        'NOS','AH','TER','VOU','ERA','SEI','SOU','DOS','ESTA','DAR','MAS','DEIXA','ESSE',
                        'QUER','QUANDO','MINHA','QUEM', 'OH', 'FOR', 'DEVE', 'TÁ', 'AÍ',
                        'TÃO', 'AAAAA', 'MIM', 'WAAAA', 'OOO', 'UOOO', 'AAAAAH', 'JÁ']
    
        for j in removeWords2:
            try:
                while True:
                    stringclear2[n2].remove(j)
            except:
                pass
        
        n2 += 1
    
    scoreList = []
    
    n3 = 0
    for i in stringclear1:
        score = []
        for l in i:
            score.append(stringclear2[n3].count(l))
    
        scoreList.append(score)
        n3 += 1
    
    n4 = 0
    for i in df2['Music']:
        df_title_music_lyric = pd.DataFrame({"Palavra": stringclear1[n4], "Contagem": scoreList[n4]})
        
        print(i, "\n")
        print(df_title_music_lyric.sort_values(by = 'Contagem', ascending = False))
        print("\n")
        
        n4 += 1
    
    print("Ao analisar os DataFrames acima, percebe-se que o título das músicas é tema recorrente nas letras.")


# Conjunto de perguntas 3 - A primeira pergunta está na parte anterior
# (Médias do tamanho das músicas por álbum)

#Média do tempo das músicas

def media_tempos(df1,df2):
    
    """    
    Prints on the console the average tempo of the songs of the entire discography.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    print("Média do tempo das músicas na discografia: ", round(df2['Time'].mean(),2),'\n')


#Gravadora mais comum, com número de vezes

def gravadora_comum(df1,df2):
    
    """    
    Prints on the console the labels most used by the band.

    :param df1: pandas.core.frame.DataFrame
    :param df2: pandas.core.frame.DataFrame

    """
    
    recorders = df1['Recorders'].value_counts().sort_values(ascending = False).head(1)
    print("Gravadora mais comum e número de vezes: \n ", recorders.to_string())

