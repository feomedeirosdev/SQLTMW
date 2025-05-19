# %%
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# %%
database_path = Path(__file__).resolve().parent.parent/'dados'/'olist.db'
engine = create_engine(f"sqlite:///{database_path}")
database_path

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
filter = df_products['product_category_name'] == 'artes'
tot_products = df_products[filter]['product_id'].count()
print(f"Total de produtos: {int(tot_products)}")

# %%
