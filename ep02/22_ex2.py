# Quantos produtos tem mais de 5 litros?

import pandas as pd
from sqlalchemy import create_engine

database_path = '../dados/olist.db'
engine = create_engine(f'sqlite:///{database_path}')

with open('21_ex2.sql', 'r') as file:
  query = file.read()

df_products = pd.read_sql(query, engine)

print(df_products.head(10))