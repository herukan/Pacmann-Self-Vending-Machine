import sqlite3
import pandas as pd

# connect to sqlite database
conn = sqlite3.connect('Pacmann_Vending.db')
cursor = conn.cursor()
print("Database has been connected")

def create_database():
    "create sqlite database if not existing"

    create_table_menu = '''CREATE TABLE IF NOT EXISTS menu (
                        menu_id INTEGER PRIMARY KEY,
                        menu_name text NOT NULL,
                        menu_price integer NOT NULL);'''

    create_table_coupon = '''CREATE TABLE IF NOT EXISTS coupon (
                            coupon_id INTEGER PRIMARY KEY,
                            coupon_name text NOT NULL,
                            coupon_rate integer NOT NULL);'''

    create_table_transaction = '''CREATE TABLE IF NOT EXISTS transactions (
                            transaction_id INTEGER PRIMARY KEY,
                            transaction_date timestamp,
                            transaction_amount integer NOT NULL,
                            deduction_amount integer,
                            coupon_amount integer);'''

    cursor.execute(create_table_menu)
    cursor.execute(create_table_coupon)
    cursor.execute(create_table_transaction)
    conn.commit()

def menu():
    """
    Function to show main menu GUI to user admin.
    """
    print("-"*50)
    print("WELCOME TO PACMANN MART SELF-SERVICES MACHINE!")
    print("*YOU ARE LOGIN IN AS ADMIN")
    print("-"*50)
    print("1. Show Menu list")
    print("2. Create New Menu")
    print("3. Delete Menu")
    print("4. Update Menu")
    print("5. Show Coupons list")
    print("6. Create New Coupons")
    print("7. Delete Coupons")
    print("8. Show Transactions list")
    print("9. Exit\n")
    
    choice = int(input('Input task number : '))
    
    try:
        if choice == 1:
            show_menu_list()
        elif choice == 2:
            create_menu()
        elif choice == 3:
            delete_menu()
        elif choice == 4:
            update_menu()
        elif choice == 5:
            show_coupon_list()
        elif choice == 6:
            create_coupon()
        elif choice == 7:
            delete_coupon()
        elif choice == 8:
            show_transactions()
        elif choice == 9:
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


def create_menu():
    """Function to create a new menu list to sell to customer.
    """
    print("-"*60)
    print("MENU CREATION")
    print("-"*60)

    menu_name = input("Input Menu Name : ")
    menu_price = input("Input Price : ")

    menu_set = (menu_name, menu_price)

    try:
        cursor.execute('INSERT INTO menu(menu_name, menu_price) VALUES (?,?)', menu_set)
        # cursor.execute("INSERT INTO menu VALUES(?, ?, ?, ?);", user)
        conn.commit()

        print("\nMenu Creation Succeed!.\n")
    except:
        print("\nMenu Creation Failed. Check your inpuut.\n")

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


def delete_menu():
    """Function to delete the menu item from database."""
 
    print("-"*50)
    print("MENU DELETE")
    print("-"*50)

    menu_id = int(input("Input Menu ID's to Delete : "))

    print(type(menu_id))

    try:
        # delete data
        sql = 'DELETE FROM menu WHERE menu_id=?'
        cursor.execute(sql, (menu_id,))
        conn.commit()

        print("\nMenu Delete Succeed!.\n")
    except:
        print("\nMenu Delete Failed. Check your input.\n")

    menu()


def update_menu():
    """Function to update the menu item from database."""

    print("-"*50)
    print("MENU UPDATE")
    print("Input Menu Item ID to update")
    print("-"*50)

    menu_id = int(input("Input Menu ID : "))
    menu_name = input("Input New Menu Name : ")
    menu_price = int(input("Input New Price : "))

    menu_set = (menu_name, menu_price, menu_id)

    try:

        sqlite_update_query = """Update menu set menu_name = ?, menu_price = ? where menu_id = ?"""
        cursor.execute(sqlite_update_query, menu_set)
        conn.commit()
        print("\nMenu Update Succeed!.\n")

    except sqlite3.Error as error:
        print("\nMenu Update Failed. Check your input.\n", error)

    menu()
    
def create_coupon():
    """Function to create a new coupon and its rate to the database."""
    
    print("-"*50)
    print("CREATE NEW COUPON")
    print("create a new coupon and its rate to the database")
    print("-"*50)

    coupon_name = input("Enter coupon name: ")
    coupon_rate = int(input("Enter coupon discount rate: "))

    coupon = (coupon_name, coupon_rate)

    try:
        cursor.execute('INSERT INTO coupon(coupon_name, coupon_rate) VALUES (?,?)', coupon)
        # cursor.execute("INSERT INTO menu VALUES(?, ?, ?, ?);", user)
        conn.commit()

        print("\nCoupon Creation Succeed!.\n")
    except:
        print("\nCoupon Creation Failed. Check your input.\n")
    
    menu()

def show_coupon_list():
    """Function to show the coupon list
    """
    try:
        # fetch all
        cursor.execute("SELECT * FROM coupon")
        all_results = cursor.fetchall()

        if not all_results:
            print("No Data found")
        else:
            df_coupon = pd.DataFrame(all_results)
            df_coupon.columns =['ID','Coupon', 'Rate']
        
            print("-"*50)
            print("Coupon List")
            print("-"*50)
            print(df_coupon)
    except:
        print("\nShow menu Failed. Check your input.\n")

    menu()

def delete_coupon():
    """Function to delete the coupon item from database."""
 
    print("-"*50)
    print("COUPON DELETE")
    print("-"*50)

    coupon_id = int(input("Input Coupon ID's to Delete : "))

    print(type(coupon_id))

    try:
        # delete data
        sql = 'DELETE FROM coupon WHERE coupon_id=?'
        cursor.execute(sql, (coupon_id,))
        conn.commit()

        print("\nCoupon Delete Succeed!.\n")
    except:
        print("\nCoupon Delete Failed. Check your input.\n")

    menu()

def show_transactions():
    """Function to show vendor transactions list
    """
    try:
        # fetch all
        cursor.execute("SELECT * FROM transactions ORDER BY transaction_date")
        all_results = cursor.fetchall()

        # zero data handling
        if not all_results:
            print("No transactions found")
        else:
            df_trans = pd.DataFrame(all_results)
            df_trans.columns =['ID','timestamp', 'transaction_amount','deduction_amount','coupon_amount']
            print("-"*60)
            print("Transactions Data")
            print("-"*60)
            print(df_trans)  

    except sqlite3.Error as error:
        print("\nTransactions Menu Failed. Check your input.\n", error)

    menu()


def main():
    "main function to execute creating database and show menu items"
    create_database()
    menu()

if __name__ == "__main__":
    main()

