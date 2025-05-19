# Ex1. Quantos produtos temos na categoria 'artes'

# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
database_path = '../dados/olist.db'
engine = create_engine(f'sqlite:///{database_path}')

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
# Filtra apenas os registros com categoria 'artes'
df_artes = df_products[df_products['product_category_name'] == 'artes']

# %%
# Aplica os cálculos
tot_linhas = len(df_artes)
tot_products_artes = df_artes['product_id'].count()
tot_products_artes_distintos = df_artes['product_id'].nunique()
qtd_categorias_distintas = df_artes['product_category_name'].nunique()

# Mostra os resultados
print({
    'tot_linhas': tot_linhas,
    'tot_products_artes': tot_products_artes,
    'tot_products_artes_distintos': tot_products_artes_distintos,
    'qtd_categorias_distintas': qtd_categorias_distintas
})

# %%
dct_artes = {
    'tot_linhas': [tot_linhas],
    'tot_products_artes': [tot_products_artes],
    'tot_products_artes_distintos': [tot_products_artes_distintos],
    'qtd_categorias_distintas': [qtd_categorias_distintas]
}

df_artes = pd.DataFrame(dct_artes)
df_artes

# %%
