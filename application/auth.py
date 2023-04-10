import bcrypt

from application.user import AuthSerializer

from domain.entities.user import User
from domain.repos.user import RepositoryUser
from adapters.infrastructure.postgresql.user import UserImpl
from main import DB as POSTGRESDB

class BaseAuth:
    """Basic class for authetication user."""
    auth : AuthSerializer
    user : User

    def __init__(self, baseuser: AuthSerializer) -> None:
        self.auth = baseuser

    def __verify_password(self) -> bool:
        if not bcrypt.checkpw(self.auth.password.encode(), self.user.password):
            return False

        return True

    def authenticate(self) -> bool:
        """Basic auth for users"""

        if self.auth.username is None or self.auth.password is None:
            return False

        repo = RepositoryUser(UserImpl(POSTGRESDB))
        self.user = repo.service_find_user(self.auth.username)

        if self.user is None:
            return False

        if not self.__verify_password():
            return False

        return True

class BasePermission:
    """Basic class for authorization user."""
    user : User

    def __init__(self, user: User) -> None:
        self.user = user

    def has_permission(self) -> bool:
        """Verify has permission for acess"""
        if self.user.is_staff:
            return True

        return False

    def has_object_permission(self, obj: any) -> bool:
        """Verify has permission for acess object"""
        if self.user.id_user == obj.id_user:
            return True

        return False
