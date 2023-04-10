from jsonpickle import decode

from domain.entities.user import User
from domain.repos.user import RepositoryUser

from adapters.infrastructure.postgresql.user import UserImpl

class AuthSerializer:
    """Auth serializer for user."""

    username: str
    password: str

    def __init__(self, data: any) -> None:
        if data is not None:
            data = decode(data.decode())

            self.username = data.get("username")
            self.password = data.get("password")


class UserSerializer:
    """Serializer for user"""

    username: str
    password: str

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def save(self) -> None:
        """Save user serializer in database postgres"""
        from main import DB as POSTGRES_DB

        user = User(self.username, self.password)
        repo = RepositoryUser(UserImpl(POSTGRES_DB))
        repo.service_save(user)
