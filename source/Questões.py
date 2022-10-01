import numpy as np
import pandas as pd

df1 = pd.read_csv('supercombo.csv')
df2 = pd.read_csv('supercombo2.csv')

#mais longas e curtas por album:

#TO DO

musicas = df2['Music']
albuns = []
duracao = []

m1 = 0
for i in musicas:
    n1 = 0
    for j in df1['Music']:
        if i in j:
            albuns.append(df1['Album'][n1])
        n1 = n1+1
    duracao.append(df2['Time'][m1])
    m1 = m1+1

df_dur_album = pd.DataFrame({'Album': albuns, 'Musica': musicas, 'Duração': duracao})

top_tempos = []
min_tempos = []

n1 = 0
for i in df1['Album']:
    tempo = []
    m1 = 0
    for j in df2['Music']:
        if (i == df_dur_album['Album'][m1]):
            tempo.append(df_dur_album['Duração'][m1])
        m1 = m1+1
    top_tempos.append(max(tempo))   
    min_tempos.append(min(tempo))
    n1 = n1+1

top_musics = []
min_musics = []

# for i in df1['Music']:
#     for j in df2['Music']:
#         if j in i:
#             for k in listtempos:
#                 for l in df_dur_album['Duração']:
#                     if l == max(k):
#                         print(j)

# print(top_musics)
# print(min_musics)

df_r_dur_album = pd.DataFrame({'Album': df1['Album'], 'Duração Maior': top_tempos, 'Duração Menor': min_tempos})

print(df_r_dur_album, "\n")



# Mais ouvidas e menos ouvidas por ámbum:

# TO DO    

visualisacoes = []
m1 = 0
for i in musicas:
    visualisacoes.append(df2['Views'][m1])
    m1 = m1+1

df_viw_album = pd.DataFrame({'Album': albuns, 'Musica': musicas, 'Visualisações': visualisacoes})

top_viw = []
min_viw = []

n1 = 0
for i in df1['Album']:
    viw = []
    m1 = 0
    for j in df2['Music']:
        if (i == df_viw_album['Album'][m1]):
            viw.append(df_viw_album['Visualisações'][m1])
        m1 = m1+1
    top_viw.append(max(viw))   
    min_viw.append(min(viw))
    n1 = n1+1

df_r_viw_album = pd.DataFrame({'Album': df1['Album'], 'Mais Visualisações': top_viw, 'Menos Visualisações': min_viw})

print(df_r_viw_album, "\n")



# Mais longa e mais curta de todas

n3 = 0
for i in df_dur_album['Duração']:
    if i == max(df_dur_album['Duração']):
        print("Maior Música: ", df_dur_album['Musica'][n3])
    if i == min(df_dur_album['Duração']):
        print("Menor Música: ", df_dur_album['Musica'][n3])
    n3 = n3+1
    
print("\n")
    


# Mais vista e menos vista de todas

n4 = 0
for i in df_viw_album['Visualisações']:
    if i == max(df_viw_album['Visualisações']):
        print("Mais Vista: ", df_viw_album['Musica'][n4])
    if i == min(df_viw_album['Visualisações']):
        print("Menos Vista: ", df_viw_album['Musica'][n4])
    n4 = n4+1

print("\n")