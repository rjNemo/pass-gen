import app.data.sqlite as sqlite
from app.data.type import DBConnector


class PasswordRepository:
    def __init__(self, db: DBConnector) -> None:
        self.db = db

    def save(self, password: str) -> None:
        try:
            self.db.execute("INSERT INTO passwords VALUES (:password)", {"password": password})
            self.db.commit()
        except Exception as e:
            print(e)


def get_instance() -> PasswordRepository:
    db = sqlite.DB()
    return PasswordRepository(db)
