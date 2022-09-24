import app.data.sqlite as sqlite
from app.data.type import DBConnector
from app.models.password import Password


class PasswordRepository:
    def __init__(self, db: DBConnector) -> None:
        self.db = db

    def save(self, service: str, password: str) -> None:
        try:
            self.db.execute(
                "INSERT INTO passwords VALUES (null, :service, :password)",
                {"service": service, "password": password},
            )

            self.db.commit()
        except Exception as e:
            print(e)

    def list_all(self) -> list[Password]:
        return [
            Password(id=row[0], service=row[1], password=row[2])
            for row in self.db.execute("SELECT * FROM passwords").fetchall()
        ]

    def exists(self, service: str) -> bool:
        row = self.db.execute(
            "SELECT EXISTS(SELECT 1 FROM passwords WHERE service=:service)",
            {"service": service},
        ).fetchone()

        return bool(row[0])


def instance() -> PasswordRepository:
    db = sqlite.DB()
    return PasswordRepository(db)
