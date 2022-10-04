# Discografia - Banda Supercombo 

[Supercombo](https://www.supercomborock.com/) é uma banda brasileira de rock alternativo. Nesse projeto, foram buscados dados sobre suas músicas e  
feitas análises para responder certas utilizando bibliotecas do Python.

## Descrição

A pasta source contém todos os códigos pyhton que foram utilizados, seja para obter os dados, seja para fazer a visualização correta deles.
Mais especificadamente: **'dados.supercombo.py'** é um arquivo Python que busca informações relativas aos álbuns de Supercombo: o seu nome, a suas músicas, o
seu ano de lançamento; **'musics_supercombo.py'** é um outro arquivo Python, que por sua busca dados sobre suas músicas: além de seu nome,
temos a sua duração(em segundos), a sua popularidade(em contagem de visualizações no [Youtube](youtube.com)(em 30 de setembro de 2022), e sua letra.
**'supercombo.csv'** e **'supercombo2.csv'** são arquivos csv's, gerados a partir de **'dados.supercombo.py'** e **'musics_supercombo.py'**, respectivamente. O primeiro
csv,em cada linha sua, apresenta informações de um álbum, enquanto o segundo apresenta informações relevantes de uma música.

***Nós recomendamos fortemente*** que abra esses arquivos .csv no LibreOffice, por exemplo, pois o Excel não os interpreta bem.

[Adicionar mais]
## Bibliotecas e programas utilizados

O programa foi construído em Python. Além de sua biblioteca padrão, necessitou-se de:
- [Chrome Driver](https://chromedriver.chromium.org/downloads) e navegador [Google Chrome](https://www.google.com/intl/pt_br/chrome/)
- [selenium](https://selenium-python.readthedocs.io/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas](https://pandas.pydata.org/docs/index.html)
- [WordCloud](https://amueller.github.io/word_cloud/)
- [Seaborn](https://seaborn.pydata.org/tutorial/introduction.html)

## Referências
- [Vagalume](https://www.vagalume.com.br/supercombo/discografia/) contém todas as letras de Supercombo.
- [Youtube](https://www.youtube.com/) foi o site utilizado para coleta de de dados sobre o tempo das músicas e visualizações(em 30 de set. de 2022).
- [Supercombo](https://www.supercomborock.com/) é o site oficial da banda.

## Contribuidores
- Max Soares
- Fernando Toledo
- Miguel Félix