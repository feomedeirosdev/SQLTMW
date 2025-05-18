# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
df_products['category_fill_na'] = df_products['product_category_name'].fillna('outros')

df_result = (
    df_products[['category_fill_na']]
    .drop_duplicates()
    .sort_values(by='category_fill_na')
    .reset_index(drop=True)
)

df_result

# %%
