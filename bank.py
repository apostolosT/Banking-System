from user import User
from account import Account
import csv
import pandas as pd


class Bank():
    def __init__(self) -> None:
        self.__users: 'list(User)' = []
        self.__accounts: 'list(Account)' = []
        self.__next_customer_number = 0
        self.__next_account_number = 0

    def register_user(self, user: 'User'):
        user.id = self.__next_customer_number
        with open("data/users.csv", "a",) as file:
            file.write('{},{},{},{},{}\n'.format(user.id, user.fname,
                                                 user.lname, user.username, user.password))
        self.__next_customer_number += 7
        self.__users.append(user)
        self._open_account(user)


    def verify_login(self, username, password):
        csv_users = csv.reader(open('data/users.csv'))
        for row in csv_users:
            print(username, password, row[3], row[4])
            if (str(row[3]) == str(username) and str(row[4]) == str(password)):
                user_id = row[0]
                current_user = [
                    c for c in self.__users if str(c.id) == user_id][0]
                if(current_user):
                    print("Login Succesful")
                    return current_user

    def _open_account(self, user: 'User'):
        self.__next_account_number += 13
        new_account = Account(user, str(self.__next_account_number))
        
        # Assign as primary account the first account that gets created for user
        if (len(user.accounts)==1):
            print("Account with id {} currently selected".format(user.accounts[0].id))
            user.current_account=user.accounts[0]

        with open("data/accounts.csv", "a",) as file:
            file.write('{},{},{}\n'.format(
                new_account.id, user.id, new_account.balance()))

        self.__accounts.append(new_account)

        # we have to add the account the account list in the Customer class
        if(new_account):
            print("Sucessfuly create account with id {} for user {}".format(
                self.__next_account_number, user.fname+user.lname))
            return True
        else:
            print("Could not create account")
            return False

    def close_account(self, acc: "Account"):
        with open('data/accounts.csv', 'rb') as inp, open('data/accounts_edit.csv', 'wb') as out:
            writer = csv.writer(out)
            deleted = False
            for row in csv.reader(inp):
                if row[0] != str(acc.id):
                    writer.writerow(row)

                else:
                    deleted = True
            if(deleted):
                print("Account with id of {} of user {} deleted".format(
                    acc.id, acc.customer.fname+acc.customer.id))

    def list_users(self):
        print([obj.__dict__ for obj in self.__users])
