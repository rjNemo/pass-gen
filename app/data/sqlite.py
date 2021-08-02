import sqlite3


class DB:
    def __init__(self, db_str="pg.db") -> None:
        self.connection = sqlite3.connect(db_str)
        self.cursor = self.connection.cursor()
        self.execute("CREATE TABLE IF NOT EXISTS passwords (password text)")

    def commit(self) -> None:
        self.connection.commit()

    def execute(self, query: str, *args) -> None:
        self.cursor.execute(query, *args)
