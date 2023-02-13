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

