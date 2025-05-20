from pandas import read_sql_table, merge
from sqlalchemy import create_engine

# Cria conexão com o banco de dados
engine = create_engine('sqlite:///../dados/olist.db')

# Carrega apenas as colunas necessárias
df_orders = read_sql_table(
  'tb_orders', 
  engine,
  columns=[
    'order_id',
    'order_status'
  ])

df_order_items = read_sql_table(
  'tb_order_items',
  engine,
  columns=[
    'order_id',
    'product_id',
    'seller_id',
    'price'
  ])

# Filtra pedidos entregues
delivered_filter = df_orders['order_status'] == 'delivered'
df_orders = df_orders[delivered_filter]

# Junta pedidos com itens
df_merged = merge(
  df_order_items,
  df_orders,
  on='order_id',
  how='inner'
)

# Agrupa por seller_id e product_id
df_seller_product = (
    df_merged
    .groupby(
      ['seller_id', 'product_id'], 
      as_index=False
    ).agg(
      qtd_product=('product_id', 'count'),
      receita=('price', 'sum')
    )
)

# Aplica ordenação por vendedor, quantidade e receita
df_seller_product_sorted = (
    df_seller_product
    .sort_values(
      ['seller_id', 'qtd_product', 'receita'], 
      ascending=[True, False, False]
    )
)

# Adiciona ranking com window function equivalente
df_seller_product_sorted['order_qtd'] = (
    df_seller_product_sorted
    .groupby('seller_id')
    .cumcount() + 1
)

# Filtra os top 5 produtos por seller
tot_filter = df_seller_product_sorted['order_qtd'] <= 1
df_top_products = df_seller_product_sorted[tot_filter]

# Seleciona colunas finais e exibe os 10 primeiros registros
df_result = df_top_products[[
  'seller_id',
  'product_id',
  'qtd_product'
]].head(10)

# Exibe o resultado
print(df_result)
