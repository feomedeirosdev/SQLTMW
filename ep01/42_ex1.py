import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

path_database = Path(__file__).resolve().parent.parent/'dados'/'olist.db'
engine = create_engine(f"sqlite:///{path_database}")

with open('41_ex1.sql', 'r') as file:
  query = file.read()

df = pd.read_sql(query, engine)

print(df)