import pandas as pd
import numpy as np

data = pd.read_excel('dados/Dados.xlsx')

data.head()

# Ordenando

data.sort_values(by='FirstName')

data.sort_values(by=['FirstName', 'LastName'])

data.sort_values(by='FirstName', ascending=False)

data.sort_values(by=['FirstName', 'LastName'], ascending=[True, False])


# Filter

df = pd.read_csv('dados/bank.csv', encoding='UTF-8', sep=';')

df.head()

df[['job','marital']].head()

df.filter(items=['job','marital']).head()

df.filter(like='day')

df.filter(regex='.day.')

##df.filter(regex='.[0-9]+')

# Operadores lógicos

df[df.marital == 'single']

df[(df.marital == 'single') & (df.education == 'primary')].head()

df.loc[(df.marital == 'single') & (df.education == 'primary'), ['age','job']].head()

df.loc[(df.marital == 'married') & 
       (df.education == 'primary') | 
       (df.education == 'secondary'), ['marital','education']].head()

# isin

df.loc[(df.marital == 'single') & (df.education.isin(['primary','secondary']))]

filtro = df.isin({'marital': ['married'], 'education':['primary','secondary']})

df[(filtro.marital) & (df.education)]

# Groupby e funções descritivas

df[df.marital == 'married'].age.mean()

df[['marital','age']].groupby('marital').mean()

df[['marital','education','age']].groupby(['marital','education']).mean() 

### Média do balanço de pessoas com idade entre 30 e 50 anos, casado e separado
df.loc[(df.age >= 30) & (df.age <= 50) ,['marital','age']].groupby('marital').mean()

df.loc[(df.age >=30) & (df.age <= 50), ['marital','education','age']].groupby(['marital','education']).mean()

# insert
df.insert(1, 'Inserindo_em_index_determinados', 'inserido na col de index 1')

# Remoção de colunas
del df['Inserindo_em_index_determinados']

# pop
coluna_excluida = df.pop('Inserindo_em_index_determinados')

# repalce, apply e applymap
alugueis = pd.read_csv('dados/houses_to_rent.csv')

alugueis['hoa'].replace('R$','') # Não funciona

alugueis['hoa_tratado'] = alugueis['hoa'].apply(lambda x: x.replace('R$','').replace(',',''))
alugueis['hoa_tratado']

alugueis[['hoa','rent amount', 'property tax']].applymap(lambda x: x.replace('R$','').replace(',',''))

# rename
alugueis.rename(columns = {'city': 'cidade', 'area': 'area_m2', 'bathroom': 'banheirtos', 'rooms': 'quartos'})

novos_nomes = ['indice','area_m2','quartos','banheiros', 'vagas_estacionamento','andar','aceita_animais','mobiliado','hoa','valor_aluguel','taxas','seguro_incendio','total']
colunas_antigas = alugueis.columns.to_list()
novas_colunas = dict(zip(colunas_antigas, novos_nomes))

alugueis.rename(columns = novas_colunas)  
       
alugueis.columns = [x.replace(' ', '_').lower() for x in alugueis.columns.to_list()]

# copy
base = alugueis.copy(deep = True)

# append
base.append({'Churros': 90}, ignore_index=True) # usar quando vc já tem uma linha inteira para colocar

# assign
base = base.assign(
       rent_amount_tratado = base['rent_amount'].apply(lambda x: x.replace('R$','').replace(',','')),
       property_tax_tratado = base['property_tax'].apply(lambda x: x.replace('R$','').replace(',',''))
)

# help
help(base.assign)

# data_range
pd.date_range('01/01/2023', periods=3)

# sample
alugueis.sample(n=5, random_state=42)

# value_counts
alugueis.furniture.value_counts()

# usando o pacote os e Path
import os
from pathlib import Path

p = Path(os.getcwd()) # pasta atual
print(p)

print(p.parent) # pasta pai

print(p.parent.parent) # pasta avô

print(str(p.parent.parent) + '\\Basico do basico\\estudado-pandas\\dados\\')

pasta_bases = str(p.parent.parent) + "\\Basico do basico\\estudado-pandas\\dados\\"
df = pd.read_csv(pasta_bases + "houses_to_rent.csv")

# sys.path
import sys

for i in sys.path:
       print(i)

# adicionando pasta no sys.path
sys.path.append('h/users/basto/Documents/Basico do basico/estudado-pandas/pastaX')


# Exportando para excel e csv
df.head()

new_df = df.loc[:10, ['city','rooms','area']]

new_df.to_excel('alugueis_teste.xlsx')
new_df.to_csv('alugueis_teste.csv', index=False)

data = pd.read_excel('alugueis_teste.xlsx', index_col=0)
data.head()

# info
df.info()

# describe
df.describe()

df.describe().T

df.describe(include=[object]).T 

del df['Unnamed: 0']

df.describe(
       percentiles=[
              0.25, 0.5, 0.75
       ]
).T

