from domain.entities.user import User
from domain.ports.user import UserInterface

class RepositoryUser:
    """Repository that receives any implementation of the user interface."""

    repos : UserInterface

    def __init__(self, repos: UserInterface) -> None:
        self.repos = repos

    def service_save(self, user: User) -> None:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.save(user)

    def service_find_user(self, username: str) -> User or None:
        """This function call calls the implementation that comes from the repository."""
        return self.repos.find_user(username)
