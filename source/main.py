import questions as q
import pandas as pd
import sys

#Leitura de arquivo
try:
    df1 = pd.read_csv('..\\dataframes\\supercombo.csv')
    df2 = pd.read_csv('..\\dataframes\\supercombo2.csv')
except FileNotFoundError as fnfe:
    print(dir(fnfe))
    print("Arquivo não existe!", fnfe)
    sys.exit()
    
    
# GRUPO DE QUESTÔES 1 EM ORDEM

q.longa_curta_album(df1, df2)

q.popular_inpopular_album(df1, df2)

q.longa_curta(df1, df2)

q.popular_inpopular_album(df1, df2)

q.premiados(df1, df2)

q.relacao_tempo_popularidade(df1, df2)


# GRUPO DE QUESTÕES 2 EM ORDEM

q.palavras_titulos_albuns(df1, df2)

q.palavras_titulos_musicas(df1, df2)

q.palavras_letras_album(df1, df2)

q.palavras_letras(df1, df2)

q.palavras_album_tema(df1, df2)

q.palavras_musica_tema(df1, df2)


# GRUPO DE QUESTÕES 3

# Média de tempo das músicas por album 
# (Respondida junto a questão 1.1)

# Média de tempo das músicas em toda discografia
q.media_tempos(df1, df2)

# Gravadora mais comum
q.gravadora_comum(df1, df2)