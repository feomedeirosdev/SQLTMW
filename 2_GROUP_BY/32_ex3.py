# crie uma coluna nova que contenha a informação de volume em m3 e reaorganize as colunas de forma diferente

import pandas as pd
from sqlalchemy import create_engine

database_path = '../dados/olist.db'
engine = create_engine(f'sqlite:///{database_path}')

with open('31_ex3.sql', 'r') as file:
  query = file.read()

df = pd.read_sql(query, engine)

print(df.head(10))
