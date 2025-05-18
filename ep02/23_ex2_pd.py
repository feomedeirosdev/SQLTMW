# Quantos produtos tem mais de 5 litros?

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
df_products['product_col_l'] = (
  df_products['product_length_cm'] *
  df_products['product_height_cm'] *
  df_products['product_width_cm'] *
  0.001)

df_products
# %%
filter = df_products['product_col_l'] > 5
df = df_products[filter]
df

# %%
dct = {
  'n_lines': [len(df)],
  'n_distinct_products': [df['product_id'].nunique()] 
}
dct

# %%
df_final = pd.DataFrame(dct)
df_final
