""" 
Análise de desempenho de vendedores:
Calcula o tempo médio (em dias) entre vendas aprovadas para cada seller.

Etapas:
1. Filtra pedidos entregues e carrega apenas colunas necessárias.
2. Junta com os itens de pedido (seller_id).
3. Calcula a diferença entre as datas de vendas consecutivas por seller.
4. Agrupa e calcula a média da diferença por seller.
5. Exibe os 10 sellers com maior e menor tempo médio entre vendas.
"""

from pandas import read_sql, to_datetime
from sqlalchemy import create_engine

# Cria conexão com o banco de dados SQLite
engine = create_engine('sqlite:///../dados/olist.db')

# Carrega apenas pedidos entregues com colunas necessárias
df_orders = read_sql(
    "SELECT order_id, order_approved_at FROM tb_orders WHERE order_status = 'delivered'",
    engine
)
df_orders['order_approved_at'] = to_datetime(df_orders['order_approved_at']).dt.date

# Carrega seller_id por pedido
df_items = read_sql(
    "SELECT order_id, seller_id FROM tb_order_items",
    engine
)

# Junta os dados
df = df_orders.merge(df_items, on='order_id', how='left')

# Remove duplicidade de vendas por seller em uma mesma data
df = df.drop_duplicates(subset=['seller_id', 'order_approved_at'])

# Ordena por seller e data
df = df.sort_values(['seller_id', 'order_approved_at'])

# Calcula defasagem da data de venda anterior
df['lag_data_venda'] = df.groupby('seller_id')['order_approved_at'].shift(1)

# Calcula diferença em dias
from pandas import to_datetime

df['order_approved_at'] = to_datetime(df['order_approved_at'])
df['lag_data_venda'] = to_datetime(df['lag_data_venda'])

df['avg_diff_dias'] = (df['order_approved_at'] - df['lag_data_venda']).dt.days

# Calcula tempo médio entre vendas por seller
df_avg = (
    df.groupby('seller_id', as_index=False)['avg_diff_dias']
    .mean()
    .rename(columns={'avg_diff_dias': 'tempo_medio_dias'})
    .round(2)
)

# 10 maiores tempos médios
top10_lentos = df_avg.sort_values(by='tempo_medio_dias', ascending=False).head(10)

# 10 menores tempos médios
top10_rapidos = df_avg.sort_values(by='tempo_medio_dias', ascending=True).head(10)

# Resultados
print("🏆 10 Sellers com maior tempo médio entre vendas:")
print(top10_lentos)

print("\n⚡ 10 Sellers com menor tempo médio entre vendas:")
print(top10_rapidos)
