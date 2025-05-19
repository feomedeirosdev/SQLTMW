# Faça uma query que apresente o tamanho médio, máximo e mínimo do nome do objeto por categoria. Considere apenas os objetos com descrição maior que 300. exiba apenasas categorias com tamanho medio de descrição do objeto maior que 100

# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
more_than_300_filter = df_products['product_description_lenght'] >= 300
df_pre_filtered = df_products[more_than_300_filter].copy()
df_pre_filtered

# %%
df_grouped = (
  df_pre_filtered
  .groupby('product_category_name')
  .agg(
    med_name_len = ('product_name_lenght', 'mean'),
    max_name_len = ('product_name_lenght', 'max'),
    min_name_len = ('product_name_lenght', 'min'),
    avg_description_len = ('product_description_lenght', 'mean')  # auxiliar para o filtro
  )
)
df_grouped

# %%
having_filter = (
    (df_grouped['avg_description_len'] > 10) |
    (df_grouped['max_name_len'] < 50)
)
df_filtered = df_grouped[having_filter].copy()
df_filtered

# %%
df_sorted = df_filtered.sort_values(
    by=['max_name_len', 'min_name_len'],
    ascending=[False, True]
)

# %%
df_sorted = df_sorted.drop(columns='avg_description_len')  # remover coluna auxiliar
df_sorted = df_sorted.round(2).reset_index()
df_sorted

# %%
