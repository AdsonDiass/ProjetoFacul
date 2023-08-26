import pandas as pd #pra fazer a biblioteca funcionar
from datetime import date
from datetime import datetime as dt


pd.Series(data=5)
lista_nomes = "Gustavo Luiz Adson Kauan Felipe".split()
pd.Series(lista_nomes)
dados = {
    'nome1' : 'Gustavo',
    'nome2' : 'Luiz',
    'nome3' : 'Adson',
    'nome4' : 'Kauan',
    'nome5' : 'Felipe',
}
pd.Series(dados) # Cria uma Series com um dicionario
print(dados)

series_dados = pd.Series([10.2,-1,None,15,23.4])
print('Quantidade de linhas = ',series_dados.shape) #Retorna uma tupla com o numero de linhas
print('Tipo de dados  ',series_dados.dtypes) #Retorna o tipo de dados, se for mistro será object
print('Os valores são unicos?  ',series_dados.is_unique) # Verifica se os valores são unicos
print('Existe valores nulos? ',series_dados.hasnans) #Retorna se existe valores nulos
print('Quantos valores existem? ',series_dados.count()) # conta quantas vvalores existem(exclui os nulos)


#DataFrame 

lista_nomes2 = "Gustavo Luiz Adson Kauan Felipe".split()

dfs = pd.DataFrame(lista_nomes2, columns=['nome'])
print(pd.DataFrame(lista_nomes2, columns=['nome']))

# o Pandas consegue ler um site e transformar em DataFrame, extrair dados 

# Criar novas colunas 

data_extracao = date.today()
dfs['data_extracao'] = data_extracao

print(dfs.info())

# to_datime serve pra converter uma coluna
# astype transforma os dados de uma coluna em um determinado tipo

data_extracao = date.today()
dfs['data_extracao'] = data_extracao
dfs['data_extracao'] = dfs['data_extracao'].astype('datetime64[ns]')

print(dfs.info())
dfs.head()










