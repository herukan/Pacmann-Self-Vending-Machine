import sqlite3
import datetime
import pandas as pd
import Transaction_Module

# connect to sqlite database
conn = sqlite3.connect('Pacmann_Vending.db')
cursor = conn.cursor()
# print("Database has been connected")

# get the timestamp and initialize Transaction class
trans_date = datetime.datetime.now()
newTransactions = Transaction_Module.Transaction(trans_date)

def menu():
    """
    Function to show main menu GUI to user customer.
    """
    
    print("-"*50)
    print("WELCOME TO PACMANN MART SELF-SERVICES MACHINE!")
    print("*YOU ARE LOGIN AS CUSTOMER")
    print("-"*50)
    print("1. Show Menu list")
    print("2. Buy Items")
    print("3. Delete Items")
    print("4. Update Items")
    print("5. Apply Coupon")
    print("6. Clear Transactions")
    print("7. Confirm Transactions")
    print("0. Exit\n")
    
    choice = int(input('Input task number : '))
    
    try:
        if choice == 1:
            show_menu_list()
        elif choice == 2:
            buy_items()
        elif choice == 3:
            delete_items()
        elif choice == 4:
            update_items()
        elif choice == 5:
            apply_coupon()
        elif choice == 6:
            clear_transaction()
        elif choice == 7:
            confirm_transaction()
        elif choice == 0:
            print("-"*50)
            print("Thank you for your transactions!.")
            print("-"*50)
            pass
        else:
            print("Wrong Input.\n")
            menu()
    except:
        print("Error, 404 Not Found.\n")
        menu()

def show_menu_list():
    """Function to show the menu list
    """

    try:
        # fetch all
        cursor.execute("SELECT * FROM menu")
        all_results = cursor.fetchall()

        if not all_results:
            print("No Data found")
        else:
            df_menu = pd.DataFrame(all_results)
            df_menu.columns =['ID','Menu', 'Price']
        
            print("-"*50)
            print("Menu List")
            print("-"*50)
            print(df_menu)
    
    except:
        print("\nShow menu Failed. Check your input.\n")

    menu()


def buy_items():
    """Function to purchase items from the database
    """
    menu_id = int(input("Enter menu ID: "))
    menu_qty = int(input("Enter quantity: "))
    newTransactions.add_transaction(menu_id,menu_qty)
    newTransactions.view_transaction()
    menu()

def delete_items():
    """Function to delete items from bucket"""
    menu_id = int(input("Enter menu ID to delete: "))
    newTransactions.delete_transaction(menu_id)
    newTransactions.view_transaction()
    menu()

def update_items():
    """Function to update items from bucket"""
    menu_id = int(input("Enter menu ID: "))
    new_id = int(input("New menu ID: "))
    menu_qty = int(input("Enter quantity: "))
    newTransactions.update_transaction(menu_id, new_id, menu_qty)
    newTransactions.view_transaction()
    menu()

def apply_coupon():
    """Function to apply coupon"""
    coupon_id = input("Enter COUPON ID: ")
    newTransactions.apply_coupon(coupon_id)
    newTransactions.view_transaction()
    menu()

def clear_transaction():
    """Function to clear the transaction"""
    newTransactions.reset_transaction()
    newTransactions.view_transaction()
    menu()

def confirm_transaction():
    """Function to confirm a transaction"""
    newTransactions.confirm_transaction()
    menu()

def main():
    "main function to execute"
    menu()

if __name__ == "__main__":
    main()