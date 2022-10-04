import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import dados_supercombo as dsc
import questions as q

#palavras mais comuns nos títulos das músicas 
all_words = q.df_contagem_letra

# gerar uma wordcloud
wordcloud = WordCloud(stopwords=all_words,
                      background_color="black",
                      width=1600, height=800).generate(all_words)

# mostrar a imagem final
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud);
wordcloud.to_file("palvras_discografia.png")

