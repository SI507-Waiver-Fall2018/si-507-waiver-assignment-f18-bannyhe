# Name: Mu He
# Uniq: bannyhe
# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

conn = sqlite3.connect('Northwind_small.sqlite')

c = conn.cursor()

if len(sys.argv) < 3:
    if sys.argv[1] == "customers":
        c.execute("SELECT id, ContactName From Customer")
        result = c.fetchall()
        print("ID\tCustomer Name")
        for customer in result:
            print(str(customer[0]) + '\t' + customer[1])
    elif sys.argv[1] == "employees":
        c.execute("SELECT id, LastName, FirstName From Employee")
        result = c.fetchall()
        print("ID\tEmployee Name")
        for customer in result:
            print(str(customer[0]) + '\t' + customer[2], customer[1])
else:
    [command, search_term] = sys.argv[2].split("=")
    if command == "cust":
        c.execute("SELECT OrderDate FROM 'Order' WHERE Customerid='{}'".format(search_term))
        result = c.fetchall()
        print("Order Dates")
        for date in result:
            print(date[0])
    elif command == "emp":
        c.execute("SELECT OrderDate FROM 'Order' WHERE Employeeid IN (SELECT id FROM Employee WHERE LastName='{}')".format(search_term))
        result = c.fetchall()
        print("Order Dates")
        for date in result:
            print(date[0])
