from typing import Any


class PasswordRepository:
    def __init__(self, db: Any) -> None:
        self.db = db

    def save(self, password: str) -> None:
        try:
            self.db.execute(f"INSERT INTO passwords VALUES (:password)", {"password": password})
            self.db.commit()
        except Exception as e:
            print(e)
