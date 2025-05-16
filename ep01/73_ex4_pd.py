# Quantos produtos de 'beleza_saude' com menos de 1 litro

# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
database_path = '../dados/olist.db'
engine = create_engine(f'sqlite:///{database_path}')

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
df_products['product_volume_litros'] = (
  df_products['product_length_cm'] *
  df_products['product_height_cm'] *
  df_products['product_width_cm'] *
  0.001
)
df_products

# %%
filter = (
  (df_products['product_category_name'] == 'beleza_saude')
  &
  (df_products['product_volume_litros'] < 1)
)

tot_products_beleza_saude_menor_1litro = df_products[filter]['product_id'].count()

# %%
print(f'Total de produdos (beleza e saúde) < 1 litro: {tot_products_beleza_saude_menor_1litro}')

# %%
