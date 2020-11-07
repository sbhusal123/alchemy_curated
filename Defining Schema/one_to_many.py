from sqlalchemy import Table, Column, create_engine, MetaData, Integer, String, DateTime
from sqlalchemy import ForeignKey, ForeignKeyConstraint

from datetime import datetime


# Meta Data for table. Can be used to create or drop tables
metadata = MetaData()

# Product Table
product_table = Table('product', metadata,
                      Column('id', Integer(), primary_key=True),
                      Column('name', String(20), index=True, unique=True),
                      Column('description', String(250), nullable=True),
                      Column('created_on', DateTime(), default=datetime.now),
                      Column('updated_on', DateTime(),
                             default=datetime.now, onupdate=datetime.now)
                      )

# Product Varient Table
product_varient_table = Table('product_varient', metadata,
                              Column('id', Integer(), primary_key=True),
                              Column('color', String(20),
                                     index=True, unique=True),
                              Column('size', String(20),
                                     index=True, unique=True),
                              Column('description', String(
                                  250), nullable=True),
                              Column('created_on', DateTime(),
                                     default=datetime.now),
                              Column('updated_on', DateTime(),
                                     default=datetime.now, onupdate=datetime.now),
                              Column('product_id', ForeignKey("product.id"))
                              # Or:  Column('product_id', ForeignKey(product_table.c.id))
                              )


# Create enginee
engine = create_engine(
    'postgres://postgres:postgres@localhost:5432/sql_alchemy')

# Shows tables in sorted order as per dependency i.e. ForeignKey
for t in metadata.sorted_tables:
    print(t.name)  # print table name

# Create all tables
metadata.create_all(engine)
