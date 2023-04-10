from domain.entities.card import Card
from domain.ports.card import CardInterface

class RepositoryCard:
    """Repository that receives any implementation of the card interface."""

    repos : CardInterface

    def __init__(self, repos: CardInterface) -> None:
        self.repos = repos

    def service_save(self, card: Card) -> None:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.save(card)

    def service_list(self) -> list[Card]:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.list()

    def service_detail(self, id_card: str) -> Card or None:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.detail(id_card)
