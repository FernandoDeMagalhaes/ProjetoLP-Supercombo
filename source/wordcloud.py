import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import dados_supercombo as dsc

#palavras mais comuns nos títulos das músicas
musics = df.dropna(['Music'])
all_musics = ''.join(m for m in musics)

stopwords = set(STOPWORDS)
stopwords.update((['o','a','os' 'as','dos']))

