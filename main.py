from user import User
from bank import Bank
from menu import Menu
from user_menu import UserMenu
from db_utils import *
import os

def main():
    # delete_all_records("users")
    # delete_all_records("accounts")


    main_menu=Menu()
    bank=Bank()
    main_menu_control=True
    
    while(main_menu_control):
        main_menu.display_menu()
        user_type:'str'=input()
        sub_menu=True
        while(sub_menu):

            if(user_type=='1'):

                main_menu.promt_registration_menu()
                registration=input()

                if(registration.lower() in ['yes','no']):

                    if(registration.lower()=='no'):
                        print("REGISTER TAB")
                        fname = input("Enter first name: ")
                        lname = input("Enter last name: ")
                        username = input("Enter username: ")
                        password = input("Enter password: ")
                        pass_check = input("Enter password again: ")
                        register=False

                        if password == pass_check:
                            print("Password match, you can login")
                            print("Registration succesfull")
                            register=True
                        
                        else:
                            print("Something Went Wrong")
                            register=False

                        if register:
                            user=User(0,fname,lname,username,password)
                            bank.register_user(user)
                            sub_menu=False
                            
                    elif(registration.lower()=='yes'):
                        print("LOGIN TAB")
                        print("Please enter username")
                        username=input()
                        print("Enter password")
                        password=input()
                        
                        user=bank.verify_login(username,password)
                        
                        if(user):
                            current_user=User(*user)
                            user_menu=UserMenu(current_user,bank)
                            user_menu.run()
                        else:
                            print("User not found")

                    else:
                        sub_menu=False
            
            elif (user_type=='2'):
                options_menu=""" Admin Actions
                             1. View user data"""
                option_input=input("Enter admin action: ")

                if (option_input==str(1)):
                    bank.list_users()

if __name__=='__main__':
    main()