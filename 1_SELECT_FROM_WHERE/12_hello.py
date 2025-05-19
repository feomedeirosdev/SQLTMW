# %%
from sqlalchemy import create_engine
import pandas as pd

# %%
# Caminho para o banco SQLite
caminho_banco = '../dados/olist.db'  # ajuste se necessário

# Criação da engine SQLAlchemy para SQLite
engine = create_engine(f'sqlite:///{caminho_banco}')

# Ler o conteúdo do arquivo hello.sql (modo texto)
with open('01_hello.sql', 'r') as file:
    query = file.read()

# %%
# Executando e carregando com Pandas
df = pd.read_sql(query, engine)

# Exibindo as 5 primeiras linhas
df.shape

# %%
