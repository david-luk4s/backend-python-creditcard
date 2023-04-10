import uuid
import bcrypt

from dataclasses import dataclass


@dataclass
class User:
    """Class for User."""
    id_user : uuid.uuid4
    username: str
    password: str
    is_staff: bool
    salt: bytes

    def __init__(self,
                 username: str,
                 password: str or bytes,
                 id_user: str = None
                 ) -> None:
        if id_user is None:
            self.id_user = uuid.uuid4()
        else:
            self.id_user =  uuid.UUID(id_user)
        self.username = username
        self.salt = b'$2b$12$5SqSGXonuxAoAeX8H6NtO.'
        if isinstance(password, str):
            self.password = self.__cript_password(password)
        else:
            self.password = password
        self.is_staff = False

    def __cript_password(self, passwd):
        hashed = bcrypt.hashpw(passwd.encode(), self.salt)
        return hashed

    def set_is_staff(self):
        """Acess staff"""
        self.is_staff = True
