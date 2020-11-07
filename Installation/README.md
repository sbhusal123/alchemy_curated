## SQL Alchemy Installation and Setup

### 1. Installating SQL Alchemy

-   `pip install sqlalchemy`

### 2. Installing DBAPI

-   DBAPI is a standard implementation that allows SQLAlchemy to interact with other databases.
-   Example: psycopg2(For postgres), mysql-python(For Mysql)
-   By default works with SQLite only.
-   Need other DBAPI and drivers to work with other databases.
-   `pip install psycopg2`

### 3. Common Terminologies:

-   **Enginee:** Allows to interact with database. Consists of two component `Dialect` and `Connection Pool`.

-   **Dialect:** Handles things like generating SQL statements, execution, result-set handling and so on for db we use.

-   **Connection Pool:** A connection factory that maintains concurrent connection. If application requires connection, ask connection pool to provide one. After performing desired action, returns connection to the pool.

## 4. Creating Enginee:

-   **Syntax for enginee string:** `dialect+driver://username:password@host:port/database`

-   Dialect refers to the database we're using. Example `mysql, postgres, oracle, ...`. Default one is used if not specified assuming it's installed.

-   Driver refers to dbapi. Example `psycopg2, python-mysql, ...`
