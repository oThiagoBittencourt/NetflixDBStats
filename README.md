# NetflixStats
### Aluno: Thiago Bittencourt Santana
![logotipo-da-netflix](https://github.com/oThiagoBittencourt/NetflixDBStats/assets/106789198/d1930b97-afc5-4225-a672-e38cab6450c1)


**Projeto acadêmico que visa analisar dados e estatísticas da Data Base do site de streaming Netflix**

### Data Base:
- Link: [NetflixDB](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Download: [netflix_titles.csv](https://github.com/oThiagoBittencourt/NetflixDBStats/files/12743825/netflix_titles.csv)

### Detalhes:
- **Número de linhas:** 8811
- **Número de colunas:** 12
- **Colunas:** show_id, type, title, director, cast, country, date_added, release_year, rating,
duration, listed_in, description
- **Imports:**
```python
import csv
import pandas as pd
import matplotlib.pyplot as plt
```

### Análises do Programa:
- **Distribuição entre filmes e séries**

Avaliação da distribuição de todos os itens do Data Frame entre o tipo filme e série de TV
```python
df['type'].value_counts().plot.barh(title='Distribuição entre filmes e séries')
```
![Figure_1](https://github.com/oThiagoBittencourt/NetflixDBStats/assets/106789198/bb13fd5d-cb4f-4ed3-87d1-541defc4c1dd)

- **Produção de filmes e séries por país**

Analise do contexto de produções referente a todos os países
```python
df['country'].value_counts().head(15).plot.pie(title='Produção de filmes e séries por país')
```
![Figure_2](https://github.com/oThiagoBittencourt/NetflixDBStats/assets/106789198/8a7f2462-787e-4c57-a64d-a4e0b387e5c2)

- **Distribuição de categorias**

Analise das principais categorias de filmes e séries presentes no catálogo da Netflix
```python
df['listed_in'].value_counts().head(15).plot.bar(title='Distribuição de categorias')
```
![Figure_3](https://github.com/oThiagoBittencourt/NetflixDBStats/assets/106789198/145b15c4-78aa-41e4-a4ec-4e34f19d38e3)

- **Quantidade total de filmes e séries por ano de produção**

Apresentação do número total de produção para cada ano referente
```python
df['release_year'].value_counts().head(20).plot.bar(title='Quantidade total de filmes e séries por ano de produção')
```
![4](https://github.com/oThiagoBittencourt/NetflixDBStats/assets/106789198/a0746d46-af62-4650-845b-2ab721550faf)

- **Dados específicos**

1. Procurar por título de filme/série
```python
titulo = input('Título: ')
print('\n', df.loc[df['title'] == titulo, ['title', 'director', 'release_year', 'duration']])
```
3. Procurar filmes/séries por ator/atriz
```python
ator = input('Ator/Atriz: ')
print('\n', df_no_null[df_no_null['cast'].str.contains(ator)])
```
5. Procurar filmes/séries por diretor(a)
```python
diretor = input('Diretor(a): ')
print('\n', df_no_null[df_no_null['director'].str.contains(diretor)])
```
