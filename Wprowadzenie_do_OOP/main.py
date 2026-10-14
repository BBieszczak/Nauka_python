from dataclasses import dataclass
from typing import List

@dataclass
class User:
    username: str
    email: str
    aktywny: bool = True

    def __str__(self) -> str:
        return f"{self.username} ({'aktywny' if self.aktywny else 'zablokowany'})"

class UserSystem:
    def __init__(self):
        self.users: list[User] = []

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def deactivate_user(self, username: str) -> bool:
        for u in self.users:
            if u.username == username:
                u.aktywny = False
                return True
        return False

    def list_users(self) -> None:
        for u in self.users:
            print(u)

if __name__ == "__main__":
    sys = UserSystem()
    sys.add_user(User("ania", "ania@example.com"))
    sys.add_user(User("bartek", "bartek@example.com"))
    sys.list_users()

    sys.deactivate_user("ania")
    sys.list_users()
