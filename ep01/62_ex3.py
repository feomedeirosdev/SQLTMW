import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

database_path = Path(__file__).resolve().parent.parent/'dados'/'olist.db'
engine = create_engine(f'sqlite:///{database_path}')

with open('61_ex3.sql', 'r') as file:
  query = file.read()

df = pd.read_sql(query, engine)

print(df.head(11))