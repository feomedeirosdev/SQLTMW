"""
Relatório de Vendas por Categoria de Produto (Ano de 2017)

Este script extrai e analisa os dados de vendas da base Olist,
considerando apenas os pedidos entregues em 2017. O objetivo é
calcular a receita, o número de itens vendidos, o número de pedidos
e a média de itens por pedido para cada categoria de produto.

Autor: Dr. Medeiros
Data: 2025-05-19
"""

# Imports mínimos e explícitos
from pandas import read_sql_table, to_datetime, merge
from sqlalchemy import create_engine

# Conexão com banco SQLite
engine = create_engine('sqlite:///../dados/olist.db')

# ------------------------------------------------------------------------------
# 1. Leitura dos dados já filtrados por colunas relevantes
# ------------------------------------------------------------------------------

# Leitura apenas das colunas necessárias para filtragem inicial
df_orders = read_sql_table(
    'tb_orders',
    engine,
    columns=['order_id', 'order_status', 'order_approved_at']
)

# Conversão para datetime e aplicação de filtro antes de merge
df_orders['order_approved_at'] = to_datetime(df_orders['order_approved_at'])

df_orders_2017 = df_orders[
    (df_orders['order_status'] == 'delivered') &
    (df_orders['order_approved_at'].dt.year == 2017)
].copy()

# ------------------------------------------------------------------------------
# 2. Leitura de itens de pedidos relacionados a esses pedidos
# ------------------------------------------------------------------------------

df_order_items = read_sql_table(
    'tb_order_items',
    engine,
    columns=['order_id', 'product_id', 'price']
)

# Filtro por pedidos válidos
df_order_items = df_order_items[
    df_order_items['order_id'].isin(df_orders_2017['order_id'])
].copy()

# ------------------------------------------------------------------------------
# 3. Leitura da tabela de produtos
# ------------------------------------------------------------------------------

df_products = read_sql_table(
    'tb_products',
    engine,
    columns=['product_id', 'product_category_name']
)

# ------------------------------------------------------------------------------
# 4. Junção das tabelas
# ------------------------------------------------------------------------------

# Merge entre pedidos e produtos
df_merged = merge(
    df_order_items,
    df_products,
    on='product_id',
    how='left'
)

# Substituição de categorias nulas
df_merged['product_category_name'] = df_merged['product_category_name'].fillna('outros')

# ------------------------------------------------------------------------------
# 5. Agregação dos dados
# ------------------------------------------------------------------------------

df_grouped = (
    df_merged
    .groupby('product_category_name', as_index=False)
    .agg(
        Receita=('price', 'sum'),
        Total_de_itens_vendidos=('product_id', 'count'),
        Total_de_pedidos=('order_id', 'nunique'),
    )
)

# Cálculo da média de itens por pedido
df_grouped = df_grouped.assign(
    Media_por_pedidos=(df_grouped['Total_de_itens_vendidos'] / df_grouped['Total_de_pedidos']).round(2)
)

# Ordenação decrescente pela média por pedido
df_resultado = df_grouped.sort_values(
    by='Media_por_pedidos',
    ascending=False,
    ignore_index=True
)

# ------------------------------------------------------------------------------
# 6. Exibição dos 10 primeiros resultados
# ------------------------------------------------------------------------------

print(df_resultado.head(10))
