<<<<<<< HEAD
import sqlite3
import csv
from tabnanny import check
from flask import Flask, request, jsonify

def connect_to_db():
    conn = sqlite3.connect('Northwind.db')
    return conn

# Operation on Product Table
def insert_Product(product_data):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''INSERT INTO Products (ProductID,ProductName,SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel,Discontinued) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?)''', 
               (product_data["ProductID"],product_data["ProductName"],product_data["SupplierID"],product_data["CatgeoryID"],product_data["QuantityPerUnit"],product_data["UnitPrice"],product_data["UnitsInStock"],product_data["UnitsOnOrder"],product_data["ReorderLevel"],product_data["Discontinued"]))
        
    conn.commit()
    return {"Product": "Inserted"}
def get_Product():
    output = []
   
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    all_product = cur.fetchall()
    # convert row objects to dictionary
    for row in all_product:
        product_data={}
        product_data["ProductID"]=row["ProductID"]
        product_data["ProductName"]=row["ProductName"]
        product_data["SupplierID"]=row["SupplierID"]
        product_data["CatgeoryID"]=row["CategoryID"]
        product_data["QuantityPerUnit"]=row["QuantityPerUnit"]
        product_data["UnitPrice"]=row["UnitPrice"]
        product_data["UnitsInStock"]=row["UNitsInStock"]
        product_data["UnitsOnOrder"]=row["UnitsOnOrder"]
        product_data["ReorderLevel"]=row["ReorderLevel"]
        product_data["Discontinued"]=row["Discontinued"]
        output.append(product_data)
    # print(output)
    return output
def get_Product_by_id(ProductID):
    product_data={}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE ProductID = ?", 
                       (ProductID,))
        row = cur.fetchone()
        # convert row object to dictionary
        if not row:
           return jsonify({'messsage': 'no customer found'})
        else:
            product_data["ProductID"]=row["ProductID"]
            product_data["ProductName"]=row["ProductName"]
            product_data["SupplierID"]=row["SupplierID"]
            product_data["CatgeoryID"]=row["CategoryID"]
            product_data["QuantityPerUnit"]=row["QuantityPerUnit"]
            product_data["UnitPrice"]=row["UnitPrice"]
            product_data["UnitsInStock"]=row["UNitsInStock"]
            product_data["UnitsOnOrder"]=row["UnitsOnOrder"]
            product_data["ReorderLevel"]=row["ReorderLevel"]
            product_data["Discontinued"]=row["Discontinued"]
    except:
        product_data={}
   
    return product_data
def update_Product(product_data):
    updated_user = {}
    
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''UPDATE products SET ProductName=?,SupplierID=?, CategoryID=?, QuantityPerUnit=?, UnitPrice=?, UnitsInStock=?, UnitsOnOrder=?, ReorderLevel=?,Discontinued=? WHERE ProductID =?''',  
                    (
                    product_data["ProductName"],
                    product_data["SupplierID"],
                    product_data["CatgeoryID"],
                    product_data["QuantityPerUnit"],
                    product_data["UnitPrice"]
                    ,product_data["UnitsInStock"]
                    ,product_data["UnitsOnOrder"]
                    ,product_data["ReorderLevel"]
                    ,product_data["Discontinued"]
                    ,product_data["ProductID"],))
    conn.commit()
    #return the user
    updated_user = get_Product_by_id(product_data["ProductID"])
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

# Operation on Product Table
def insert_Product(product_data):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''INSERT INTO Products (ProductID,ProductName,SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel,Discontinued) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?)''', 
               (product_data["ProductID"],product_data["ProductName"],product_data["SupplierID"],product_data["CatgeoryID"],product_data["QuantityPerUnit"],product_data["UnitPrice"],product_data["UnitsInStock"],product_data["UnitsOnOrder"],product_data["ReorderLevel"],product_data["Discontinued"]))
        
    conn.commit()
    return {"Product": "Inserted"}
def get_Product():
    output = []
   
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    all_product = cur.fetchall()
    # convert row objects to dictionary
    for row in all_product:
        product_data={}
        product_data["ProductID"]=row["ProductID"]
        product_data["ProductName"]=row["ProductName"]
        product_data["SupplierID"]=row["SupplierID"]
        product_data["CatgeoryID"]=row["CategoryID"]
        product_data["QuantityPerUnit"]=row["QuantityPerUnit"]
        product_data["UnitPrice"]=row["UnitPrice"]
        product_data["UnitsInStock"]=row["UNitsInStock"]
        product_data["UnitsOnOrder"]=row["UnitsOnOrder"]
        product_data["ReorderLevel"]=row["ReorderLevel"]
        product_data["Discontinued"]=row["Discontinued"]
        output.append(product_data)
    # print(output)
    return output
def get_Product_by_id(ProductID):
    product_data={}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE ProductID = ?", 
                       (ProductID,))
        row = cur.fetchone()
        # convert row object to dictionary
        if not row:
           return jsonify({'messsage': 'no customer found'})
        else:
            product_data["ProductID"]=row["ProductID"]
            product_data["ProductName"]=row["ProductName"]
            product_data["SupplierID"]=row["SupplierID"]
            product_data["CatgeoryID"]=row["CategoryID"]
            product_data["QuantityPerUnit"]=row["QuantityPerUnit"]
            product_data["UnitPrice"]=row["UnitPrice"]
            product_data["UnitsInStock"]=row["UNitsInStock"]
            product_data["UnitsOnOrder"]=row["UnitsOnOrder"]
            product_data["ReorderLevel"]=row["ReorderLevel"]
            product_data["Discontinued"]=row["Discontinued"]
    except:
        product_data={}
   
    return product_data
def update_Product(product_data):
    updated_user = {}
    
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''UPDATE products SET ProductName=?,SupplierID=?, CategoryID=?, QuantityPerUnit=?, UnitPrice=?, UnitsInStock=?, UnitsOnOrder=?, ReorderLevel=?,Discontinued=? WHERE ProductID =?''',  
                    (
                    product_data["ProductName"],
                    product_data["SupplierID"],
                    product_data["CatgeoryID"],
                    product_data["QuantityPerUnit"],
                    product_data["UnitPrice"]
                    ,product_data["UnitsInStock"]
                    ,product_data["UnitsOnOrder"]
                    ,product_data["ReorderLevel"]
                    ,product_data["Discontinued"]
                    ,product_data["ProductID"],))
    conn.commit()
    #return the user
    updated_user = get_Product_by_id(product_data["ProductID"])
    return updated_user
if __name__ == '__main__':
>>>>>>> faecfc5bd35e0c9e68f76409f8510f35eb5885e9
    get_Product()