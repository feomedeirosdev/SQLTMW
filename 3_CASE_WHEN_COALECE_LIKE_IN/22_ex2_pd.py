# Faça uma query que apresente o tamanho médio, máximo e mínimo do nome do objeto por categoria

# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
df = (
  df_products
  .groupby('product_category_name')
  .agg(
    name_lenght_min = ('product_name_lenght', 'min'),
    name_lenght_max = ('product_name_lenght', 'max'),
    name_lenght_med = ('product_name_lenght', 'mean'),
  )
  .round(2)
  .reset_index()
)
df
# %%
