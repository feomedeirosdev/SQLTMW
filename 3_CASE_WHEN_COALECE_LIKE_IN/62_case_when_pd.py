# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
df_products['fill_na_category'] = df_products['product_category_name'].fillna('outros')
df_products

# %%
df_unique_sorted = (
  df_products[['fill_na_category']]
  .drop_duplicates()
  .sort_values(by='fill_na_category')
  .reset_index(drop=True)
).copy()
df_unique_sorted 
# %%
