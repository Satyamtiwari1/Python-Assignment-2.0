<<<<<<< HEAD
import sqlite3
import csv
from tabnanny import check
from flask import Flask, request, jsonify

def connect_to_db():
    conn = sqlite3.connect('Northwind.db')
    return conn


def insert_customer(customer_data):
    inserted_user = {}
   
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''INSERT INTO customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?)''', (customer_data['CustomerID'],
        customer_data['CompanyName'],
        customer_data['ContactName'],
        customer_data['ConatctTitle'],
        customer_data['Address'],
        customer_data['City'],
        customer_data['Region'],
        customer_data['PostalCode'],
        customer_data['Country'],
        customer_data['Phone'],
        customer_data['Fax']))
    conn.commit()
    return {"Message": "Inserted"}
def get_customer():
    output = []
   
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    all_customer = cur.fetchall()
    print(all_customer)
    # convert row objects to dictionary
    for row in all_customer:
        customer_data={}
        customer_data['CustomerID']=row["CustomerID"]
        customer_data['CompanyName']=row["CompanyName"]
        customer_data['ContactName']=row["ContactName"]
        customer_data['ConatctTitle']=row["ContactTitle"]
        customer_data['Address']=row["Address"]
        customer_data['City']=row["City"]
        customer_data['Region']=row["Region"]
        customer_data['PostalCode']=row["PostalCode"]
        customer_data['Country']=row["Country"]
        customer_data['Phone']=row["Phone"]
        customer_data['Fax']=row["Fax"]
        output.append(customer_data)
    # print(output)
    return output
def get_customer_by_id(CustomerID):
    customer_data={}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE CustomerID = ?", 
                       (CustomerID,))
        row = cur.fetchone()
        # convert row object to dictionary
        if not row:
           return jsonify({'messsage': 'no customer found'})
        else:
            customer_data['CustomerID']=row["CustomerID"]
            customer_data['CompanyName']=row["CompanyName"]
            customer_data['ContactName']=row["ContactName"]
            customer_data['ConatctTitle']=row["ContactTitle"]
            customer_data['Address']=row["Address"]
            customer_data['City']=row["City"]
            customer_data['Region']=row["Region"]
            customer_data['PostalCode']=row["PostalCode"]
            customer_data['Country']=row["Country"]
            customer_data['Phone']=row["Phone"]
            customer_data['Fax']=row["Fax"]
    except:
        customer_data={}
    print(customer_data)
    return customer_data
def update_customer(customer_data):
    updated_user = {}
    
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''UPDATE customers SET CompanyName = ?, ContactName = ?, ContactTitle = 
                    ?, Address = ?, City= ?,Region=?,PostalCode=?,Country=?,Phone=?,Fax=? WHERE CustomerID =?''',  
                    (
        customer_data['CompanyName'],
        customer_data['ContactName'],
        customer_data['ConatctTitle'],
        customer_data['Address'],
        customer_data['City'],
        customer_data['Region'],
        customer_data['PostalCode'],
        customer_data['Country'],
        customer_data['Phone'],
        customer_data['Fax'],
        customer_data['CustomerID'],))
    conn.commit()
    #return the user
    updated_user = get_customer_by_id(customer_data["CustomerID"])
    return updated_user
if __name__ == '__main__':
=======
import sqlite3
import csv
from tabnanny import check
from flask import Flask, request, jsonify

def connect_to_db():
    conn = sqlite3.connect('Northwind.db')
    return conn


def insert_customer(customer_data):
    inserted_user = {}
   
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''INSERT INTO customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?)''', (customer_data['CustomerID'],
        customer_data['CompanyName'],
        customer_data['ContactName'],
        customer_data['ConatctTitle'],
        customer_data['Address'],
        customer_data['City'],
        customer_data['Region'],
        customer_data['PostalCode'],
        customer_data['Country'],
        customer_data['Phone'],
        customer_data['Fax']))
    conn.commit()
    return {"Message": "Inserted"}
def get_customer():
    output = []
   
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")
    all_customer = cur.fetchall()
    print(all_customer)
    # convert row objects to dictionary
    for row in all_customer:
        customer_data={}
        customer_data['CustomerID']=row["CustomerID"]
        customer_data['CompanyName']=row["CompanyName"]
        customer_data['ContactName']=row["ContactName"]
        customer_data['ConatctTitle']=row["ContactTitle"]
        customer_data['Address']=row["Address"]
        customer_data['City']=row["City"]
        customer_data['Region']=row["Region"]
        customer_data['PostalCode']=row["PostalCode"]
        customer_data['Country']=row["Country"]
        customer_data['Phone']=row["Phone"]
        customer_data['Fax']=row["Fax"]
        output.append(customer_data)
    # print(output)
    return output
def get_customer_by_id(CustomerID):
    customer_data={}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE CustomerID = ?", 
                       (CustomerID,))
        row = cur.fetchone()
        # convert row object to dictionary
        if not row:
           return jsonify({'messsage': 'no customer found'})
        else:
            customer_data['CustomerID']=row["CustomerID"]
            customer_data['CompanyName']=row["CompanyName"]
            customer_data['ContactName']=row["ContactName"]
            customer_data['ConatctTitle']=row["ContactTitle"]
            customer_data['Address']=row["Address"]
            customer_data['City']=row["City"]
            customer_data['Region']=row["Region"]
            customer_data['PostalCode']=row["PostalCode"]
            customer_data['Country']=row["Country"]
            customer_data['Phone']=row["Phone"]
            customer_data['Fax']=row["Fax"]
    except:
        customer_data={}
    print(customer_data)
    return customer_data
def update_customer(customer_data):
    updated_user = {}
    
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''UPDATE customers SET CompanyName = ?, ContactName = ?, ContactTitle = 
                    ?, Address = ?, City= ?,Region=?,PostalCode=?,Country=?,Phone=?,Fax=? WHERE CustomerID =?''',  
                    (
        customer_data['CompanyName'],
        customer_data['ContactName'],
        customer_data['ConatctTitle'],
        customer_data['Address'],
        customer_data['City'],
        customer_data['Region'],
        customer_data['PostalCode'],
        customer_data['Country'],
        customer_data['Phone'],
        customer_data['Fax'],
        customer_data['CustomerID'],))
    conn.commit()
    #return the user
    updated_user = get_customer_by_id(customer_data["CustomerID"])
    return updated_user
if __name__ == '__main__':
>>>>>>> faecfc5bd35e0c9e68f76409f8510f35eb5885e9
    get_customer()