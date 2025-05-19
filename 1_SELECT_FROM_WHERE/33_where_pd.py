# %%
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# %%
path_database = Path(__file__).resolve().parent.parent/'dados'/'olist.db'
engine = create_engine(f"sqlite:///{path_database}")
path_database

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
select = ['product_id', 'product_category_name', 'product_photos_qty']
df_products = df_products[select]
df_products

# filtros:
# - categoria 'bebes' acima de 1 foto 
# - ou categoria 'perfumaria' acima de 5 fotos
where = (
  ((df_products['product_category_name'] == 'bebes') & (df_products['product_photos_qty'] > 1))
  |
  ((df_products['product_category_name'] == 'perfumaria') & (df_products['product_photos_qty'] > 5))
)
# %%
df = df_products[where]
df
# %%
