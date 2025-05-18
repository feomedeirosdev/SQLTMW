# Liste as categorias por ordem alfabética

# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
df_products[['product_category_name']].nunique()


# %%
df_sorted = (
    df_products[['product_category_name']]
    .dropna()  # se quiser excluir os NaN
    .drop_duplicates()
    .sort_values(by='product_category_name')
    .reset_index(drop=True)
)
df_sorted

# %%
