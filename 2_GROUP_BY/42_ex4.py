# Quantos produtos de "beleza_saude" com menos de 1 litro

import pandas as pd
from sqlalchemy import create_engine

database_path = '../dados/olist.db'
engine = create_engine(f'sqlite:///{database_path}')

with open('41_ex4.sql', 'r') as file:
  query = file.read()

df = pd.read_sql(query, engine)

print(df)