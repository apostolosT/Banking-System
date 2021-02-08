from user import User
from bank import Bank
from menu import Menu
from user_menu import UserMenu
import os

# def create_account(bank:'Bank',user:'User'):
#     bank.open_account(user)

# user_actions={'1':create_account}



def main():
    if("users.csv" in os.listdir('data') and "accounts.csv" in os.listdir('data')):
        os.remove("data/accounts.csv")
        os.remove("data/users.csv")

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
                        user=User()
                        login=user.register()
                        if login:
                            bank.register_user(user)
                            sub_menu=False
                        
                    elif(registration.lower()=='yes'):
                        print("LOGIN TAB")
                        print("Please enter username")
                        username=input()
                        print("Enter password")
                        password=input()
                        
                        user:'User'=bank.verify_login(username,password)

                        if(user):
                            user_menu=UserMenu(user,bank)
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