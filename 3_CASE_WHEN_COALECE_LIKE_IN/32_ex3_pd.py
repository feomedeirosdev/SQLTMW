# Faça uma query que mostre o tamanho médio, máximo e mínimo do nome do objeto por categoria. Considere apenas os objetos que tenham a descrição maiorque 50

# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
more_than_50_filter = df_products['product_description_lenght'] >= 100

# %%
df_filtered = df_products[more_than_50_filter]
df_filtered

# %%
df = (
  df_filtered
  .groupby('product_category_name')
  .agg(
    min_name_len = ('product_name_lenght', 'min'),
    max_name_len = ('product_name_lenght', 'max'),
    med_name_len = ('product_name_lenght', 'mean'),
  )
)

df
