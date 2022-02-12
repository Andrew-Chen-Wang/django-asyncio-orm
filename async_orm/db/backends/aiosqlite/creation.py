from async_orm.db.backends.base.creation import BaseAsyncDatabaseCreation
from async_orm.db.backends.sqlite3.creation import (
    DatabaseCreation as SQLiteDatabaseCreation,
)


class DatabaseCreation(BaseAsyncDatabaseCreation, SQLiteDatabaseCreation):
    pass
