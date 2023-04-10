from abc import ABC, abstractmethod

from domain.entities.user import User

class UserInterface(ABC):
    """Interface to define which user contract should follow."""

    @classmethod
    @abstractmethod
    def save(cls, user: User) -> None:
        """This abstract function what defines what behavior should follow"""

    @classmethod
    @abstractmethod
    def find_user(cls, username: str) -> User or None:
        """This abstract function what defines what behavior should follow"""
