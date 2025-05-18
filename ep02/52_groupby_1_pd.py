# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
engine = create_engine('sqlite:///../dados/olist.db')

# %%
df_products = pd.read_sql_table('tb_products', engine)
df_products

# %%
# Filtrando o DataFrame
filtro = (
    df_products['product_category_name'].notna() &
    (df_products['product_category_name'] != 'artes') &
    (df_products['product_category_name'] != 'bebes')
)

# %%
df_filtrado = df_products[filtro].copy()
df_filtrado

# %%
# Criando a coluna de peso em kg
df_filtrado['product_weight_kg'] = df_filtrado['product_weight_g'] / 1000
df_filtrado

# %%
# Agrupando e calculando as estatísticas
df_resultado = (
    df_filtrado
    .groupby('product_category_name')
    .agg(
        qtd_produtos_distintos=('product_id', 'nunique'),
        maior_peso_kg=('product_weight_kg', 'max'),
        menor_peso_kg=('product_weight_kg', 'min'),
        media_peso_kg=('product_weight_kg', 'mean')
    )
    .round(2)
    .reset_index()
)

df_resultado

# %%
