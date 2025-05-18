# Ex1. Quantos produtos temos na categoria 'artes'

import pandas as pd
from sqlalchemy import create_engine

database_path = '../dados/olist.db'
engine = create_engine(f'sqlite:///{database_path}')

with open('11_ex1.sql', 'r') as file:
  query = file.read()

df = pd.read_sql(query, engine)

print(df)