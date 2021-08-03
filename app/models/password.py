from pydantic import BaseModel, SecretStr


class Password(BaseModel):
    id: int
    service: str
    password: SecretStr

    class Config:
        anystr_strip_whitespace = True
