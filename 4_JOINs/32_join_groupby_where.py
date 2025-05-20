# Considerando as vendas de 2017 e pedidos entregues
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
  on='product_id',
  how='left'
)

list(df_merged.columns)

# %%
df_orders = pd.read_sql_table('tb_orders', engine)
list(df_orders.columns)

# %%
df_merged_2 = pd.merge(
  df_merged,
  df_orders,
  on='order_id',
  how='left'
)

list(df_merged_2.columns)
# %%
df_merged_2['order_approved_at'] = pd.to_datetime(df_merged_2['order_approved_at'])

type(df_merged_2['order_approved_at'][0])

# %%
order_status_filter = df_merged_2['order_status'] == 'delivered'
order_approved_at_filter = df_merged_2['order_approved_at'].dt.year == 2017

# %%
df_filtred = df_merged_2[order_status_filter & order_approved_at_filter].copy()
df_filtred

# %%
df_filtred['product_category_name'] = df_filtred['product_category_name'].fillna('outros')

# %%
df_grouped = (
  df_filtred
  .groupby('product_category_name')
  .agg(
    Receita = ('price', 'sum'),
    Total_de_itens_vendidos = ('product_id', 'count'),
    Total_de_pedidos = ('order_id', 'nunique'),
  )
  .reset_index()
)

df_grouped

# %%
df_grouped['Media_por_pedidos'] = (
  df_grouped['Total_de_itens_vendidos'] / df_grouped['Total_de_pedidos']
).round(2)

df_grouped

# %%
df = df_grouped.sort_values(
  by='Media_por_pedidos', 
  ascending=False,
  ignore_index=True).copy()

df.head(10) #mostrar as 10 categorias mais promissoras pra fazer promoção

