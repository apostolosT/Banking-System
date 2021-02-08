from typing import TYPE_CHECKING
if TYPE_CHECKING:  
    from user import User
    from bank import Bank
    from account import Account

def create_account(bank:'Bank',user:'User'):
    bank._open_account(user)


