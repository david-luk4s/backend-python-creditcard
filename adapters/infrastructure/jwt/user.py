import jwt

from domain.entities.user import User
from config.settings import SECRET_KEY

class BaseJWT:
    """Class base for Json Web Tokens."""
    user : User

    def __init__(self, user: User) -> None:
        self.user = user

    def generator_token(self) -> str:
        """Encode payload in jwt."""
        payload = {
            "id_user": str(self.user.id_user),
            "username": self.user.username,
            "is_staff": self.user.is_staff
        }
        encoded = jwt.encode(payload, SECRET_KEY, algorithm="HS256"
        )
        return encoded

    @staticmethod
    def decode_token(encoded) -> str:
        """Decode and Validate token."""
        try:
            decoded = jwt.decode(encoded, SECRET_KEY, algorithms=["HS256"])
            return decoded
        except jwt.InvalidSignatureError:
            return {"message": "invalid signature"}
        except jwt.DecodeError:
            return {"message": "invalid signature"}
