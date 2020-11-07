## Defining Schemas

### 1. Creating Database Tables

-   Database tables represented by the instance of Table(`sqlalchemy.Table`) Class.

-   Table constructor accepts metadata and one or column instance(`sqlalchemy.Column`) arguments with constraints.

-   MetaData(`sqlalchemy.Metadata`) objects holds information about the tables. We use it's instance to create or drop tables.

```python
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean
from datetime import datetime

foo_table = Table('foo_table', metadata,
    Column('id', Integer(), primary_key=True),
    Column('bar1', String(200), nullable=False),
    Column('bar1', Text(),  nullable=False),
    Column('bar2', Boolean(),  default=False),
    Column('created_on', DateTime(), default=datetime.now)
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)
```

**Meta data methods**

```python
# Tables
for t in metadata.tables:
    print(metadata.tables[t])

# Sorted Table as per dependencies (ForeignKey).
for t in metadata.sorted_tables:
    print(t.name)

# Create all tables
metadata.create_all(enginee)
```

#### 1.1 Column Level Constraints:

-   `primary_key`: Composite primary key
-   `nullable`: Can be null value?
-   `default`: Default value if not specified
-   `Unique`: Needs to be unique(Boolean)?
-   `index`: Need table to be indexed by the column ? (Boolean)
-   `autoincreament`: Auto increament value: (Boolean)
-   `onupdate`: What to do on update? (Callable/function/method)

### 1.2. Column Type:

-   [Generic Types](https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-core/#generic-types)
-   [SQL Standard Types](https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-core/#sql-standard-types)
-   [Vendor Specific Types](https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-core/#vendor-specific-types)

### 1.3. Table Label Constraints

-   Can be imported directly from sqlalchemy
-   `PrimaryKeyConstraint`: Import `sqlalchemy.PrimaryKeyConstraint`.
-   `ForeignKeyConstraint`: Import `sqlalchemy.ForeignKeyConstraint`
-   `UniqueConstraint`: Import `sqlalchemy.ForeignKeyConstraint`
-   `CheckConstraint`: Import `sqlalchemy.CheckConstraint`
-   `Index`: Import `sqlalchemy.Index`

**ForeignKeyConstraint**

```python
parent = Table('foo', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(16), nullable=False)
)

child = Table('bar', metadata,
    Column('id', Integer, primary_key=True),
    Column('parent_id', Integer, nullable=False),
    Column('name', String(40), nullable=False),
    ForeignKeyConstraint(['parent_id'],['foo.id'])
)
```

**UniqueConstraint**

```python
foo = Table('foo', metadata,
    Column('foo1', Integer, primary_key=True),
    Column('foo2', Integer, nullable=False),
    Column('foo4', String(16), nullable=False),
    UniqueConstraint('foo1', 'foo2', name='uniq_together') # unique together
)
```

**CheckConstraint**

```python
foo = Table('foo', metadata,
    Column('id', Integer(), primary_key=True),
    Column('bar1', String(100), nullable=False),
    Column('bar2', Integer(), nullable=False),
    CheckConstraint('bar2 < 100000', name='bar2_check')
)
```
