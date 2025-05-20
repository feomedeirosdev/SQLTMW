# Qual é a receita de cada categoria do produto?
# e o total em vendas?
# em unidades e em pedidos

# %%
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../dados/olist.db')

# %%
df_order_items = pd.read_sql_table('tb_order_items', engine)
df_products = pd.read_sql_table('tb_products', engine)

# %%
df_order_items

# %%
df_products

# %%
df_merged = pd.merge(
  df_order_items,
  df_products,
  on='product_id',
  how='left'
)
df_merged.head(1)

# %%
list(df_merged.columns)

# %%
interest_columns = [
  'order_id',
  'order_item_id',
  'product_id',
  # 'seller_id',
  # 'shipping_limit_date',
  # 'price',
  # 'freight_value',
  'product_category_name',
  # 'product_name_lenght',
  # 'product_description_lenght',
  # 'product_photos_qty',
  # 'product_weight_g',
  # 'product_length_cm',
  # 'product_height_cm',
  # 'product_width_cm'
  ]

df = df_merged[interest_columns]

# %%
df
# %%
