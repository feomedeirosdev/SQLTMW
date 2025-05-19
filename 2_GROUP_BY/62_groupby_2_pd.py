# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
# criando coluna product_weight_kg
df_products['product_weight_kg'] = (df_products['product_weight_g'] 
                                    * 0.001)
df_products

# %%
na_filter = df_products['product_category_name'].isna()
categorys_filter = (df_products['product_category_name'].isin (['artes', 'bebes'])) 

# %%
df_products_fitered = df_products[na_filter | categorys_filter].copy()
df_products_fitered 

# %%
df = (
  df_products_fitered
  .groupby('product_category_name', dropna=False)
  .agg(
    qtd_distinct_products = ('product_id', 'nunique'),
    weight_min = ('product_weight_kg', 'min'),
    weight_max = ('product_weight_kg', 'max'),
    weight_mean = ('product_weight_kg', 'mean'),
  )
  .round(2)
  .reset_index()
)

df


# %%
