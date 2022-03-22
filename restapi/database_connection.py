<<<<<<< HEAD
import sqlite3
import csv


class Database:
    def __init__(self):
        self.con = sqlite3.connect("northwind.db")
        self.cur = self.con.cursor()

    def create_tables(self):
            query1='''create table customers (CustomerID varchar(100) primary key,CompanyName varchar(100),ContactName varchar(100),ContactTitle varchar(100),Address varchar(100),
            City varchar(100),Region varchar(100),PostalCode varchar(100),Country varchar(100),Phone varchar(100),Fax varchar(100))'''
            self.cur.execute(query1)
            self.con.commit()
            query2='''create table products (ProductID int primary key,ProductName varchar(100),SupplierID int,CategoryID int,QuantityPerUnit varchar(100),UnitPrice real,UnitsInStock int,
            UnitsOnOrder int,ReorderLevel int,Discontinued boolean)'''
            self.cur.execute(query2)
            self.con.commit()
            query3='''create table orders (OrderID int primary key,CustomerID varchar(100),EmployeeID int,OrderDate date,RequiredDate date,ShippedDate date,
            ShipVia int,Freight real,ShipName varchar(100),ShipAddress varchar(100),ShipCity varchar(100),ShipRegion varchar(100),ShipPostalCode varchar(100),ShipCountry varchar(100))'''
            self.con.execute(query3)
            self.con.commit()
        
    def customer_table(self):
        # For customer.csv
        file=open('Northwind_database_csv\customers.csv')
        contents=csv.reader(file)
        insert_record="insert into Customers values(?,?,?,?,?,?,?,?,?,?,?)"
        self.cur.executemany(insert_record,contents)
        self.con.commit()
    def product_table(self):
        # For Product Table
        file=open('Northwind_database_csv\products.csv')
        contents=csv.reader(file)
        insert_record="insert into Products values(?,?,?,?,?,?,?,?,?,?)"
        self.cur.executemany(insert_record,contents)
        self.con.commit()
    def order_table(self):
        # For Order Table
        file=open('Northwind_database_csv\orders.csv')
        contents=csv.reader(file)
        insert_record="insert into Orders values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        self.cur.executemany(insert_record,contents)
        self.con.commit()

    def check_data(self):
        self.cur.execute('select * from orders;')
        print(self.cur.fetchall())
        
if __name__ == '__main__':
    D=Database()
    # D.create_tables()
    # D.customer_table()
    # D.product_table()
    # D.order_table()
=======
import sqlite3
import csv


class Database:
    def __init__(self):
        self.con = sqlite3.connect("northwind.db")
        self.cur = self.con.cursor()

    def create_tables(self):
            query1='''create table customers (CustomerID varchar(100) primary key,CompanyName varchar(100),ContactName varchar(100),ContactTitle varchar(100),Address varchar(100),
            City varchar(100),Region varchar(100),PostalCode varchar(100),Country varchar(100),Phone varchar(100),Fax varchar(100))'''
            self.cur.execute(query1)
            self.con.commit()
            query2='''create table products (ProductID int primary key,ProductName varchar(100),SupplierID int,CategoryID int,QuantityPerUnit varchar(100),UnitPrice real,UnitsInStock int,
            UnitsOnOrder int,ReorderLevel int,Discontinued boolean)'''
            self.cur.execute(query2)
            self.con.commit()
            query3='''create table orders (OrderID int primary key,CustomerID varchar(100),EmployeeID int,OrderDate date,RequiredDate date,ShippedDate date,
            ShipVia int,Freight real,ShipName varchar(100),ShipAddress varchar(100),ShipCity varchar(100),ShipRegion varchar(100),ShipPostalCode varchar(100),ShipCountry varchar(100))'''
            self.con.execute(query3)
            self.con.commit()
        
    def customer_table(self):
        # For customer.csv
        file=open('Northwind_database_csv\customers.csv')
        contents=csv.reader(file)
        insert_record="insert into Customers values(?,?,?,?,?,?,?,?,?,?,?)"
        self.cur.executemany(insert_record,contents)
        self.con.commit()
    def product_table(self):
        # For Product Table
        file=open('Northwind_database_csv\products.csv')
        contents=csv.reader(file)
        insert_record="insert into Products values(?,?,?,?,?,?,?,?,?,?)"
        self.cur.executemany(insert_record,contents)
        self.con.commit()
    def order_table(self):
        # For Order Table
        file=open('Northwind_database_csv\orders.csv')
        contents=csv.reader(file)
        insert_record="insert into Orders values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        self.cur.executemany(insert_record,contents)
        self.con.commit()

    def check_data(self):
        self.cur.execute('select * from orders;')
        print(self.cur.fetchall())
        
if __name__ == '__main__':
    D=Database()
    # D.create_tables()
    # D.customer_table()
    # D.product_table()
    # D.order_table()
>>>>>>> faecfc5bd35e0c9e68f76409f8510f35eb5885e9
    D.check_data()