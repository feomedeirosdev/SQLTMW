
#%%
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# %%
# Caminho dinâmico para o arquivo olist.db
caminho_banco = Path(__file__).resolve().parent.parent/'dados'/'olist.db'
caminho_banco

# %%
# Criação da engine SQLite
engine = create_engine(f"sqlite:///{caminho_banco}")

# %%
# Lista de tabelas
tabelas = [
  'tb_customers',
  'tb_orders',
  'tb_geolocation',
  'tb_product_category_name_translation',
  'tb_order_items',
  'tb_products',
  'tb_order_payments',
  'tb_sellers',
  'tb_order_reviews',
  'tb_sellers_cluster'
]

# %%
# Dicionário para armazenar os DataFrames com prefixo 'df_'
dfs = {f"df_{nome[3:]}": pd.read_sql(f"SELECT * FROM {nome}", engine) for nome in tabelas}

# %%
# Exemplo de como acessar um DataFrame
df_customers = dfs['df_customers']
df_orders = dfs['df_orders']
df_geolocation = dfs['df_geolocation']
df_product_category_name_translation = dfs['df_product_category_name_translation']
df_order_items = dfs['df_order_items']
df_products = dfs['df_products']
df_order_payments = dfs['df_order_payments']
df_sellers = dfs['df_sellers']
df_order_reviews = dfs['df_order_reviews']
df_sellers_cluster = dfs['df_sellers_cluster']

# %%
df_customers

# %%
