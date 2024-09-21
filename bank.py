from tkinter import *
from tkinter import messagebox
import os
import time


def root():
    print('''Welcome to Azeem National Bank
            Press 1 to open an account
            press 2 to make deposit
            press 3 to make withdrawal
            press 4 to check balance
            press 5 to quit app''')
    gen()

    
    
def gen():
    root1 = Tk()
    root1.title("BANK")
    root1.config(padx=150,pady=150)

    def check_balance():
        password = int(input("Enter Password To Check Balance: "))
        confirm_password = int(input("Enter to confirm Password: "))
        if password != confirm_password:
            print('Invalid!')
            clear_time()
            check_balance()
            print("please Kindly Wait For Procession...")
            clear_time()
            print("Your Accont Balance Is **** Naira remaining")

    def make_withdrawal():
        witdraw = int(input("Enter Amount To Be Withdrawn: "))
        password = int(input("Enter Your Password: "))
        confirm_password = int(input("Enter to confirm Password: "))
        if password != confirm_password:
            print('Invalid!')
            clear_time()
            make_withdrawal()
            print(f'''Amount to be witdrawed is {witdraw}
                  Your withdrawal is being proccessed...''')
            clear_time()
            print(f'Withdrawal Successful\nYou Have Successfully Witdrawn {witdraw} Naira')
            clear_time()


    def make_deposit():
        amount = int(input('Enter Amount: '))
        password = int(input("Enter your password: "))
        confirm = print(f'Amount to be deposited is {amount}\nWait while transaction is processing...')
        clear_time()
        print('Deposit Successful!')
    
    def quit_app():
        print("Thanks for your time")

    def open_account():
        global bvn
        firstname = input('Enter First name: ')
        lastname = input('Enter last name ')
        phonenumber = int(input('Enter your phone number: '))
        password = input('Enter your Password: ')
        confirm_password = input('Confirm your password: ')
        if password != confirm_password:
            print('Invalid!')
            open_account()
        else:
            bvn = int(input('Enter your bvn: '))
            print('Account Created Successfully!\nKindly wait for your account number')
            clear_time()
            print(f'{firstname} {lastname} Your account number is 01{bvn}')
            print('Do you want to make a deposit?\n select option 2 to make deposit or select 5 to quit app ')
            clear_time()
            menu()

    def menu():
        option = int(input('Enter your option: '))
        if option == 1:
            open_account()
        elif option == 2:
            make_deposit()
        elif option == 3:
            make_withdrawal()
        elif option == 4:
            check_balance()
        elif option == 5:
            quit_app()
        else:
            print('You made an invalid selection')
        menu()

    def clear_time():
        time.sleep(5)
        os.system('cls')

if __name__ == '__main__':
    root()