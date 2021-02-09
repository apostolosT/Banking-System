from db_utils import get_acc_id, get_balance
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from account import Account
    from bank import Bank


class User():
    def __init__(self, id: int, fname, lname, username, password) -> None:
        self.fname: str = fname
        self.lname: str = lname
        self.username: str = username
        self.password: str = password
        self.id = id

    def current_account(self):
        from account import Account
        acc_id = get_acc_id(self.id)
        balance = get_balance(acc_id)
        user_account = Account(acc_id, balance)
        return user_account
