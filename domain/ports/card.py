from abc import ABC, abstractmethod

from domain.entities.card import Card

class CardInterface(ABC):
    """Interface to define which card contract should follow."""

    @classmethod
    @abstractmethod
    def save(cls, card: Card) -> None:
        """This abstract function what defines what behavior should follow"""

    @classmethod
    @abstractmethod
    def list(cls) -> list[Card]:
        """This abstract function what defines what behavior should follow"""

    @classmethod
    @abstractmethod
    def detail(cls, id_card: str) -> Card or None:
        """This abstract function what defines what behavior should follow"""
