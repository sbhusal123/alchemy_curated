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

#### 1.1 Column Level Constraints:

-   `primary_key`: Composite primary key
-   `nullable`: Can be null value?
-   `default`: Default value if not specified
-   `Unique`: Needs to be unique(Boolean)?
-   `index`: Need table to be indexed by the column ? (Boolean)
-   `autoincreament`: Auto increament value: (Boolean)
