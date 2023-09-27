import csv
import pandas as pd
import matplotlib.pyplot as plt

# Gerando o Data Frame a partir do CSV
df = pd.read_csv("netflix_titles.csv")

# Fazendo a limpeza de arquivos duplicados e vazios do DF
df.drop_duplicates(inplace = True)
df_no_null = df.dropna().copy()

# Pesquisas específicas do DF
def dados_especificos():
    while True:
        try:
            entrada = int(input('\n1. Procurar por filme/série\n2. Procurar por ator\n3. Procurar por diretor\n0. VOLTAR\n'))
        except:
            print('\nInsira um valor válido!')
            continue
        match (entrada):
            case 1:
                # Pesquisa no DF pelo título do filme/série
                titulo = input('Título: ')
                print('\n', df.loc[df['title'] == titulo, ['title', 'director', 'release_year', 'duration']])
            case 2:
                # Pesquisa no DF pelo ator/atriz
                ator = input('Ator/Atriz: ')
                print('\n', df_no_null[df_no_null['cast'].str.contains(ator)])
            case 3:
                # Pesquisa no DF pelo diretor/diretora
                diretor = input('Diretor(a): ')
                print('\n', df_no_null[df_no_null['director'].str.contains(diretor)])
            case 0:
                break

print("\nEstatísticas Netflix")
while True:
    try:
        entrada = int(input('\n1. Distribuição entre filmes e séries\n2. Produção de filmes e séries por país.\n3. Distribuição de categorias\n4. Quantidade total de filmes e séries por ano de produção\n5. Dados específicos\n0. SAIR\n'))
    except:
        print('\nInsira um valor válido!')
        continue
    match (entrada):
        case 1:
            # Gráfico que apresenta a distribuição do DF entre filmes e séries de TV
            df['type'].value_counts().plot.barh(title='Distribuição entre filmes e séries')
            plt.show()
        case 2:
            # Gráfico pizza que apresenta os 15 países com maior número de produção de filmes e séries na netflix
            df['country'].value_counts().head(15).plot.pie(title='Produção de filmes e séries por país')
            plt.show()
        case 3:
            # Gráfico apresentando as 15 categorias mais presentes no site
            df['listed_in'].value_counts().head(15).plot.bar(title='Distribuição de categorias')
            plt.show()
        case 4:
            # Gráfico com os 20 anos de maior lançamento dos filmes e séries do DF
            df['release_year'].value_counts().head(20).plot.bar(title='Quantidade total de filmes e séries por ano de produção')
            plt.show()
        case 5:
            # Execução de pesquisas mais específicas no DF, apresentando interação com o usuário
            dados_especificos()
        case 0:
            print('\nEncerrando o Programa...')
            break