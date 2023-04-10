import uuid

from dataclasses import dataclass
from datetime import date

@dataclass
class Card:
    """Class for keeping track of item in cards."""
    id_card : uuid.uuid4
    exp_date: date
    holder: str
    number : str
    cvv: int
    brand: str

    def __init__(self,
                 exp_date: date,
                 holder: str,
                 number: str,
                 cvv: int,
                 brand: str,
                 id_card: str = None
        ) -> None:
        if id_card is None:
            self.id_card = uuid.uuid4()
        else:
            self.id_card =  uuid.UUID(id_card)
        self.exp_date = exp_date
        self.holder = holder
        self.number = number
        self.cvv = cvv
        self.brand = brand
