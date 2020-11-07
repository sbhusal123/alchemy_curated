from sqlalchemy import create_engine


# Create a enginee: Reference: https://overiq.com/sqlalchemy-101/installing-sqlalchemy-and-connecting-to-database/#some-additional-arguments
engine = create_engine(
    "postgres+psycopg2://postgres:postgres@localhost:5432/sql_alchemy",
    echo=True, pool_size=6, max_overflow=10, encoding='latin1')

"""
Parameters description:
- echo: Optional: A boolean argument if set to True, the engine will log all the SQL it is currently executing to the standard output. 
                 By default, it is set to False.

- pool_size: Option: specifies the number of connection to keep in the connection pool. Its default value is 5.

- max_overflow: Option: specifies the number of connections that can be opened beyond the pool_size setting, 
                by default it is set to 10.

- encoding: Optional: specifies the encoding to use by SQLAlchemy. By default, it is set to utf-8. 
                      Note that it doesn't control the encoding scheme of the database.

- isolation_level: Optiona: Defines isolation level to use
"""

# Connect to database
engine.connect()

print(engine)
