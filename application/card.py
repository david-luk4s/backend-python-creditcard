import re
import calendar
from datetime import date

import cryptography.fernet
from jsonpickle import decode

from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound

from domain.entities.card import Card
from config.settings import SECRET_KEY

class CardSerializer:
    """Serializer for card."""

    data = any

    def __init__(self, data: any = None) -> None:
        if data is not None and bool(data.decode()):
            self.data = decode(data)

    def __required_fields(self) -> bool:
        requireds = ["exp_date", "holder", "number"]
        all_keys = self.data.keys()

        for reqkey in requireds:
            if reqkey not in all_keys:
                return False

        return True

    def __format_holder(self) -> bool:
        if len(self.data["holder"]) <= 2:
            return False

        return True

    def __format_exp_date(self) -> bool:
        date_pattern = "^[0-9]{1,2}\\/[0-9]{4}$"
        match_date = re.match(date_pattern, self.data["exp_date"])

        if match_date is None:
            return False

        month, year = match_date.string.split("/")
        _, last_day = calendar.monthrange(int(year), int(month))

        self.data["exp_date"] = date(year=int(year), month=int(month), day=last_day)

        return True

    def __set_exp_date_isoformat(self, card: Card) -> None:
        card.exp_date = card.exp_date.isoformat()

    def __format_cvv(self) -> bool:
        if self.data.get("cvv"):
            if len(self.data.get("cvv")) < 3 or len(self.data.get("cvv")) > 4:
                return False

            self.data["cvv"] = int(self.data["cvv"])

        return True

    def __convert_id_card(self, card: Card) -> None:
        card.id_card = str(card.id_card)

    def __find_brand(self) -> None:
        try:
            credit_card = CreditCard(self.data["number"])
            self.data["brand"] = credit_card.get_brand()
        except BrandNotFound:
            self.data["brand"] = ""

    def __crypto_card_number(self) -> None:
        fcry = cryptography.fernet.Fernet(SECRET_KEY.encode())
        self.data["number"] = fcry.encrypt(self.data["number"].encode()).decode()

    def is_valid(self) -> bool:
        """Check data is valid"""

        # Check required fields
        if not self.__required_fields():
            print("fail required fields")
            return False

        # Check holder field
        if not self.__format_holder():
            print("fail format holder")
            return False

        # Format expire date
        if not self.__format_exp_date():
            print("fail format exp_date")
            return False

        # Check if date not expired
        if self.data["exp_date"].year <= date.today().year and \
            self.data["exp_date"].month < date.today().month:
            print("fail expired exp_date")
            return False

        # Check cvv valid
        if not self.__format_cvv():
            print("fail format cvv")
            return False

        # Check card is valid with lib CreditCard
        if not CreditCard(self.data["number"]).is_valid():
            print("fail validate card")
            return False

        return True

    def process_card(self) -> Card:
        """process card"""

        self.__find_brand()

        self.__crypto_card_number()

        card = Card(
            exp_date=self.data["exp_date"],
            holder=self.data["holder"],
            number=self.data["number"],
            cvv=self.data.get("cvv"),
            brand=self.data["brand"])

        self.__set_exp_date_isoformat(card)

        self.__convert_id_card(card)

        return card
