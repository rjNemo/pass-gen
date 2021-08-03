import sqlite3
from typing import Any


class DB:
    def __init__(self, db_str: str = "pg.db") -> None:
        self.connection = sqlite3.connect(db_str)
        self.cursor = self.connection.cursor()
        self.execute(
            "CREATE TABLE IF NOT EXISTS passwords (id integer PRIMARY KEY , service text UNIQUE NOT NULL, "
            "password text NOT NULL)"
        )

    def commit(self) -> None:
        self.connection.commit()

    def execute(self, query: str, *args: Any) -> sqlite3.Cursor:
        return self.cursor.execute(query, *args)
