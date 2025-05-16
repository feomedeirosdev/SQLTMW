
# %%
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# %%
database_path = '../dados/olist.db'
engine = create_engine(f'sqlite:///{database_path}')
database_path

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
df = df_products.copy()

df['product_volume_litros'] = (
  df['product_length_cm'] *
  df['product_height_cm'] *
  df['product_width_cm']
)

df_products
# %%
df