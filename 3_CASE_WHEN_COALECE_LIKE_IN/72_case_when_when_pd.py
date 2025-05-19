# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
def categorizar(nome):
    if pd.isna(nome):
        return 'outros'
    elif nome in ['alimentos', 'alimentos_bebidas']:
        return 'alimentos'
    elif nome in ['artes', 'artes_e_artesanato']:
        return 'artes'
    elif 'artigos' in nome:
        return 'artigos'
    else:
        return nome

# %%
# Aplicando a função
df_products['category_fill_na'] = df_products['product_category_name'].apply(categorizar)

# Pegando valores únicos e ordenando
df_unique_sorted = (
    df_products[['category_fill_na']]
    .drop_duplicates()
    .sort_values(by='category_fill_na')
    .reset_index(drop=True)
)

df_unique_sorted

# %%
df_grouped = (
    df_products
    .groupby('category_fill_na')
    .agg(qtd_produtos=('product_id', 'count'))
    .reset_index()
    .sort_values(by='category_fill_na')
)

df_grouped
# %%
