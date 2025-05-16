# %%
from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

# %%
path_database = Path(__file__).resolve().parent.parent/'dados'/'olist.db'
engine = create_engine(f"sqlite:///{path_database}")
path_database

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products.head(10)

# %%
df_products.columns

# %%
columns = ['product_id', 'product_category_name', 'product_photos_qty']
df = df_products[columns]
df.head(10)


