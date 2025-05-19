# Quantos produtos tem mais de 5 litros?

# %%
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# %%
database_path = Path(__file__).resolve().parent.parent/'dados'/'olist.db'
engine = create_engine(f'sqlite:///{database_path}')
database_path

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
df_products['product_volume_litros'] = (
  df_products['product_length_cm'] * 
  df_products['product_height_cm']*
  df_products['product_width_cm'] *
  0.001)

df_products
# %%
select = ['product_id', 'product_volume_litros']
df = df_products[select]
df

# %%
