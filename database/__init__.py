import databases
from playhouse.postgres_ext import PostgresqlExtDatabase

database = PostgresqlExtDatabase(
    'gulshantelkar',  # Your database name
    user='gulshantelkar',  # Your PostgreSQL username
    password='',  # Your PostgreSQL password
    host='localhost',
    port=5432
)
