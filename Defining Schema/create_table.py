from sqlalchemy import Table, Column, create_engine, MetaData, Integer, String, DateTime
from datetime import datetime


# Meta Data for table. Can be used to create or drop tables
metadata = MetaData()


# Table accepts name, metadata obj, columns as arguments
user_table = Table('user', metadata,
                   Column('id', Integer(), primary_key=True),
                   Column('name', String(20), index=True),
                   Column('username', String(20), unique=True),
                   Column('contact', Integer(), unique=True),
                   Column('description', String(250), nullable=True),
                   Column('created_on', DateTime(), default=datetime.now),
                   Column('updated_on', DateTime(),
                          default=datetime.now, onupdate=datetime.now)
                   )


# Show list of all columns
print(user_table.columns)  # or  print(user_table.c)

# Show list of tables
for t in metadata.tables:
    print(metadata.tables[t])

# Create enginee
engine = create_engine(
    'postgres://postgres:postgres@localhost:5432/sql_alchemy')

# Create all tables
metadata.create_all(engine)
