# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')

# %%
df_products = pd.read_sql_table('tb_products', engine)

# %%
df = (
  df_products
  .groupby('product_category_name')
  .agg(
    description_lenght_min = ('product_description_lenght', 'min'),
    description_lenght_max = ('product_description_lenght', 'max'),
    description_lenght_med = ('product_description_lenght', 'mean'),
  )
  .round(2)
  .reset_index()
)
df
