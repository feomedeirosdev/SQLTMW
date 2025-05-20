# Qual é a receita de cada categoria do produto?
# e o total em vendas?
# em unidades e em pedidos

# %%
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../dados/olist.db')

# %%
df_order_items = pd.read_sql_table('tb_order_items', engine)
list(df_order_items.columns)

# %%
df_products = pd.read_sql_table('tb_products', engine)
list(df_products.columns)

# %%
df_merged = pd.merge(
  df_order_items,
  df_products,
  on = 'product_id',
  how = 'left'
)
list(df_merged.columns)

# %%
df_merged['product_category_name'] = df_merged['product_category_name'].fillna('outros')

# %%
df_grouped = (
  df_merged
  .groupby('product_category_name')
  .agg(
    receita = ('price', 'sum'),
    total_de_itens_vendidos = ('product_id', 'count'),
    total_de_pedidos = ('order_id', 'nunique'),
  )
  .reset_index()
)

# %%
df_grouped['media_pedidos'] = (
  df_grouped['total_de_itens_vendidos'] / df_grouped['total_de_pedidos']
).round(2)

df = df_grouped.sort_values(by='media_pedidos', ascending=False).copy()

# %%
df


# %%
