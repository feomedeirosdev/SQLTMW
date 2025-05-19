# Quantos produtos de "beleza_saude" com menos de 1 litro

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
  pow(10, -3))
df_products

# %%
beleza_saude_filter = df_products['product_category_name'] == 'beleza_saude'
volume_filter = df_products['product_col_l'] < 1

df_filtrado = df_products[beleza_saude_filter & volume_filter]
df_filtrado

# %%
# Armazenamento temporário
dct = {
  'n_linhas': [len(df_filtrado)],
  'qtd_produt_ids': [df_filtrado['product_id'].count()], 
  'qtd_distinct_product_ids': [df_filtrado['product_id'].nunique()],
  'qtd_distinct_category_name': [df_filtrado['product_category_name'].nunique()]
}
dct
# %%
df = pd.DataFrame(dct)
df
# %%
