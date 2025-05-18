# dbutils/connection.py

from sqlalchemy import create_engine

def conectar_sqlite(caminho_banco: str):
    """
    Cria e retorna um engine SQLAlchemy para um banco SQLite.

    Parâmetros:
        caminho_banco (str): Caminho relativo ou absoluto para o arquivo .db.

    Retorna:
        sqlalchemy.engine.base.Engine: engine conectado ao banco SQLite.
    """
    engine = create_engine(f"sqlite:///{caminho_banco}")
    return engine
