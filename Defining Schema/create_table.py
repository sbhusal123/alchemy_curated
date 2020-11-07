from sqlalchemy import Table, Column, create_engine, MetaData, Integer, String


# Meta Data for table. Can be used to create or drop tables
metadata = MetaData()


# Table accepts name, metadata obj, columns as arguments
user_table = Table('user', metadata,
                   Column('id', Integer(), primary_key=True),
                   Column('name', String(20), primary_key=True),
                   )


# Show list of all columns
print(user_table.columns)  # or  print(user_table.c)

# Create enginee
engine = create_engine(
    'postgres://postgres:postgres@localhost:5432/sql_alchemy')

# Create all tables
metadata.create_all(engine)
