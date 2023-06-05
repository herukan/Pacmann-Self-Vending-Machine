import sqlite3
import datetime
import pandas as pd

# connect to sqlite database
conn = sqlite3.connect('Pacmann_Vending.db')
cursor = conn.cursor()
# print("Database has been connected")

class Transaction:
    """Class representing a transaction that is currently in progress
    
    ATTRIBUTES:
    trans_list: list of transaction consist of id, name, qty, and amount
    coupon: coupon amount that added to the transaction
    coupon_name: name of coupon
    deduction: deduction rate for the transaction
    final_price: final price of the transaction
    """
    trans_list = {}
    coupon = 0
    coupon_name = ""
    deduction = 0
    final_price = 0

    def __init__(self, date):
        self.date = date

    def add_transaction(self, menu_id, quantity):
        """Function to add a transaction item to the list"""
        
        try:
            sql = 'SELECT * FROM menu WHERE menu_id=?'
            cursor.execute(sql, (menu_id,))
            all_results = cursor.fetchall()
            self.trans_list.update({menu_id: {'Nama':all_results[0][1], 'Harga_pcs':all_results[0][2], 'Jumlah':quantity, 'Harga_total':(all_results[0][2]*quantity)}})
        except:
            print("Error 404")

    def view_transaction(self):
        """Function to view whole transaction of the list"""
        if self.trans_list:
            df_test = pd.DataFrame(self.trans_list.values())
            print("-"*50)
            print("Bucket List")
            print("-"*50)
            s = pd.Series(self.trans_list.keys())
            print(df_test.set_index(s))
        else:
            print("-"*50)
            print("Bucket List Empty")
            print("-"*50)
     
    def delete_transaction(self, menu_id):
        """Function to delete an item from transaction list"""
        try:
            self.trans_list.pop((menu_id))
            print("Item Deleted Successfully")
        except:
            print("Item Delete Failed")

    def update_transaction(self, menu_id, new_id, quantity):
        """Function to update an item from transaction list"""
        try:
            sql = 'SELECT * FROM menu WHERE menu_id=?'
            cursor.execute(sql, (new_id,))
            all_results = cursor.fetchall()
            self.trans_list.update({menu_id: {'Nama':all_results[0][1], 'Harga_pcs':all_results[0][2], 'Jumlah':quantity, 'Harga_total':(all_results[0][2]*quantity)}})
            print("Item Updated Successfully")
        except:
             print("\nTransaction Failed. Check your input.\n")


    def reset_transaction(self):
        """Function to reset transaction"""
        try:
            self.trans_list.clear()
            print("Bucket List Clear Successfully")
        except:
            print("\nTransaction Failed. Check your input.\n")

    def apply_coupon(self, coupon):
        """Function to apply couupon to the transaction and checking the coupon availability in the database"""
        # fetch all
        cursor.execute("SELECT * FROM coupon")
        all_results = cursor.fetchall()

        # check if coupon already exists
        for row in all_results:
            
            if row[1] == coupon:
                self.coupon = row[2]
                self.coupon_name = row[1]
                break
            else:
                print("ini else")
                self.coupon = 0
        
        if self.coupon == 0:
            print("-"*50)
            print("Coupon not found!")
            print("-"*50)
        elif self.coupon > 0:
            print("-"*50)
            print(f"Coupon '{coupon}' with rate of {self.coupon}% applied!")
            print("-"*50)
        
    def confirm_transaction(self):
        """Function to confirming a transaction, showing final bucket status and deduction rate 
        
        ATTRIBUTE:
        fix_price : total fixed price deducted by coupon
        deduction_rate : deduction rate
        total_price = total raw original price
        """
        fix_price = 0
        deduction_rate = 0
        total_price = 0

        self.view_transaction()

        # accummulating price
        for i in self.trans_list.values():
            total_price += i['Harga_total']

        # appplying deduction rate 
        if total_price > 200000:
            deduction_rate = 5
            fix_price = total_price - (total_price * ((5/100) + (self.coupon/100)))
        elif total_price > 300000:
            deduction_rate = 8
            fix_price = total_price - (total_price * ((8/100) + (self.coupon/100)))
        elif total_price > 500000:
            deduction_rate = 10
            fix_price = total_price - (total_price * ((10/100) + (self.coupon/100)))

        print("-"*50)
        print(f"Total Price: {total_price}")
        print(f"Total Discount: {deduction_rate + self.coupon}%")
        print(f"Coupon Used: '{self.coupon_name}'")
        print(f"Final Price: {fix_price}")
        print("-"*50)

        final_trans = (self.date, fix_price, deduction_rate, self.coupon)

        try:
            cursor.execute('INSERT INTO transactions(transaction_date, transaction_amount, deduction_amount, coupon_amount) VALUES (?,?,?,?)', final_trans)
            conn.commit()

            print("\nTransaction Succeed!.\n")
        except:
            print("\nTransaction Failed. Check your input.\n")