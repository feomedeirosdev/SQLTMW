# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = ('sqlite:///../dados/olist.db')

# %%
df_sellers = pd.read_sql_table('tb_sellers', engine)
df_sellers

# %%
df = (
  df_sellers
  .groupby('seller_state')
  .agg(
    qtd_sellers = ('seller_id', 'nunique')
  )
  .reset_index()
)
df

# %%
sellers_filter = df['qtd_sellers'] >= 10

# %%
df = df[sellers_filter]
df
# Esse era o objetivo final, resgatar todos os estados commais de 10 vendedores.O where seller_state in ('AC', 'AM', 'RJ', 'SP', 'PR', 'ES') no sql era só pra mostrar as ordens dos filtros.Mas eu vou fazer tambem

# %%
df_sellers = pd.read_sql_table('tb_sellers', engine)
df_sellers

# %%
state_filter = df_sellers['seller_state'].isin(['AC', 'AM', 'RJ', 'SP', 'PR', 'ES'])

# %%
df_pre_filtered = df_sellers[state_filter].copy()
df_pre_filtered

# %%
df_grouped = (
  df_pre_filtered
  .groupby('seller_state')
  .agg(
    qtd_sellers = ('seller_id', 'nunique')
  ).reset_index()
)
df_grouped

# %%
more_than_10_sellers_filter = (df_grouped['qtd_sellers'] >= 10)

# %%
df_post_filtered = df_grouped[more_than_10_sellers_filter].copy()
df_post_filtered

# Perdoe o nome das variáveis tão explícitas, eu tava fazendo desse jeito como se fosse pra me explicar o que era cada coisa kkkk. Existe uma certa desavença na comunidade, uns preferem nomes de variáveis bem explicadas para evitar comentários, outro preferem variáveis menores com comentérios pra evitar um código mais verboso (caso tenha que chamar aquela variável muitas vezes). Eu ainda não sei o que prefiro. Acho que vai depender do caso. 
