# crie uma coluna nova que contenha a informação de volume em m3 e reaorganize as colunas de forma diferente

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
df_products['product_volume_m3'] = (
  (df_products['product_length_cm'] *
  df_products['product_height_cm'] *
  df_products['product_width_cm']) /
  pow(10,6))

df_products

# %%
lst_cols = list(df_products.columns)
lst_cols

# %%
new_order_list_cols = [
  'product_id',
  'product_category_name',
  'product_volume_m3',
  'product_name_lenght',
  'product_description_lenght',
  'product_photos_qty',
  'product_weight_g',
  'product_length_cm',
  'product_height_cm',
  'product_width_cm',]

# %%
df = df_products[new_order_list_cols]
df

