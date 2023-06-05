# Python Project: Self-Service Machine Pacmann Mart

### A. Background

Self Service Vending machine software to be used for customer self transactions in PacmannMart, will be used for customer self transactions and administrative to create list of menu products and coupon information, software featuring database to store transaction information history that can be used for administrative to  analyze in future work.

<img src="assets\Feature.jpg" width="1000"/>

### B. Tools
Languages: 
* Python
* SQL

Libraries Required: 
* sqlite3
* Pandas
* datetime

### C. Objective

Learning objective: 
* Implement Python knowledge to be used for building software to be used for customer
* Using OOP to create Python program
* Creating logical Flowchart to be used for designing software
* Appy PEP8 principles to write clean Python program 

Program objective: 
* Building Create, Update, Read, Delete (CRUD) system for administration to manage menu items to sell and its price
* Building Function  to show transaction information history to analyze in future works
* Building Coupon management system for administration to give to the customer
* Building self service system for customers to show menu, choose, buy and manage the market bucket, and dispalying transaction information

### D. Program Description 

1. Create SQL LITE Database on the workspace
    * Create DB named "Pacmann_Vending.db" containing 3 tables
    * Table 1 - menu: Contain menu information 
    * Table 2 - coupon: Contain coupon information
    * Table 3 - transactions: Contain transactions history information 
    * Output: "Pacmann_Vending.db" file

_Diagram 1: ERD for Pacmann_Vending.db
<img src="assets\ERD.jpg" width="1000"/>


2. Create Program Flowchart
    _Digram 2: Flowchart_
    <img src="assets\Flowchart.jpg" width="1000"/>

### E. Guide to Try It Yourself 

1. Clone/downlaod this git repository into your local computer.
2. Run "Admin_Module.py" to run system as administrator to manage menu items to sell, and it will initialize the database.
3. Run Customer_Module.py to run as customer to start a self service transactions.

### E. Module Description

1. Admin_Module.py: Handle the menu items to sell to customer and the coupon that can be applied and show transactions data history.
2. Transaction_Module.py: Handle Customer bucket's CRUD operation on Customer_Module.py.
3. Customer_Module.py: Manage customer transactions activity by handling GUI to user.
    

### F. Test Cases & Results

__Test case 1: Administrator Section__
1.A: Main menu
    <img src="assets\Admin\Screenshot 2023-06-04 151918.png" width="1000"/>
1.B: Display Menu List 
    <img src="assets\Admin\Screenshot 2023-06-04 151938.png" width="1000"/>
1.C: Display Coupon List and rate
    <img src="assets\Admin\Screenshot 2023-06-04 152009.png" width="1000"/>
1.D: Display Transaction History List 
    <img src="assets\Admin\Screenshot 2023-06-04 152023.png" width="1000"/>

__Test case 2: Customer Section__
2.A: Input Items to buy
    <img src="assets\Customer\Screenshot 2023-06-04 152329.png" width="1000"/>
2.B: Deleting an item in bucket list
    <img src="assets\Customer\Screenshot 2023-06-04 152410.png" width="1000"/>
2.C: Updating Items in bucket list
    <img src="assets\Customer\Screenshot 2023-06-04 152455.png" width="1000"/>
2.D: Applying Coupon to the transaction
    <img src="assets\Customer\Screenshot 2023-06-04 152540.png" width="1000"/>
2.E: Clearing Transaction Bucket list
    <img src="assets\Customer\Screenshot 2023-06-04 152607.png" width="1000"/>
2.F: Confirming Transacation and showing transaction detail
    <img src="assets\Customer\Screenshot 2023-06-04 152804.png" width="1000"/>


# Conclusion/Future Works
1. Developing Transcation history data management in administrator section.
2. Developing Coupon Status that can be disable or enable to apply in customer side
3. Python Basic functionality, modularity and OOP programming has been successfully implemented in the program


__Author__
Copyright (c) _2023_ _Heru Mulyana_