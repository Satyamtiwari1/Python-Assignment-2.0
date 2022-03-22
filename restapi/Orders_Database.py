<<<<<<< HEAD
import sqlite3
import csv
from tabnanny import check
from flask import Flask, request, jsonify

def connect_to_db():
    conn = sqlite3.connect('Northwind.db')
    return conn

# Operation on Product Table
def insert_Orders(data):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''INSERT INTO Orders (OrderID,CustomerID,EmployeeID,OrderDate,RequiredDate,ShippedDate,ShipVia,Freight,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry
) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?,?,?,?)''', 
               (data["OrderID"],data["CustomerID"],data["EmployeeID"],
               data["OrderDate"],
            data["RequiredDate"],data["ShippedDate"],data["ShipVia"],data["Freight"],
            data["ShipName"],data["ShipAddress"],data["ShipCity"],data["ShipRegion"],
            data["ShipPostalCode"],data["ShipCountry"]))
        
    conn.commit()
    return {"Orders": "Inserted"}
def get_Orders():
    output = []
   
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    all_orders = cur.fetchall()
    # convert row objects to dictionary
    for row in all_orders:
        data={}
        data["OrderID"]=row["OrderID"]
        data["CustomerID"]=row["CustomerID"]
        data["EmployeeID"]=row["EmployeeID"]
        data["OrderDate"]=row["OrderDate"]
        data["RequiredDate"]=row["RequiredDate"]
        data["ShippedDate"]=row["ShippedDate"]
        data["ShipVia"]=row["ShipVia"]
        data["Freight"]=row["Freight"]
        data["ShipName"]=row["ShipName"]
        data["ShipAddress"]=row["ShipAddress"]
        data["ShipCity"]=row["ShipCity"]
        data["ShipRegion"]=row["ShipRegion"]
        data["ShipPostalCode"]=row["ShipPostalCode"]
        data["ShipCountry"]=row["ShipCountry"]
        output.append(data)
    # print(output)
    return output
def get_Order_by_id(OrderID):
    data={}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Orders WHERE OrderID = ?", 
                       (OrderID,))
        row = cur.fetchone()
        # convert row object to dictionary
        if not row:
           return jsonify({'messsage': 'no customer found'})
        else:
            data["OrderID"]=row["OrderID"]
            data["CustomerID"]=row["CustomerID"]
            data["EmployeeID"]=row["EmployeeID"]
            data["OrderDate"]=row["OrderDate"]
            data["RequiredDate"]=row["RequiredDate"]
            data["ShippedDate"]=row["ShippedDate"]
            data["ShipVia"]=row["ShipVia"]
            data["Freight"]=row["Freight"]
            data["ShipName"]=row["ShipName"]
            data["ShipAddress"]=row["ShipAddress"]
            data["ShipCity"]=row["ShipCity"]
            data["ShipRegion"]=row["ShipRegion"]
            data["ShipPostalCode"]=row["ShipPostalCode"]
            data["ShipCountry"]=row["ShipCountry"]
    except:
        data={}
   
    return data
def update_Order(data):
    updated_user = {}
    
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''UPDATE Orders SET CustomerID=?,EmployeeID=?,OrderDate=?,RequiredDate=?,ShippedDate=?,ShipVia=?,Freight=?,ShipName=?,ShipAddress=?,ShipCity=?,ShipRegion=?,ShipPostalCode=?,ShipCountry=? WHERE OrderID =?''',  
                    (data["CustomerID"],
                    data["EmployeeID"],data["OrderDate"],
            data["RequiredDate"],data["ShippedDate"],data["ShipVia"],data["Freight"],
            data["ShipName"],data["ShipAddress"],data["ShipCity"],data["ShipRegion"],
            data["ShipPostalCode"],data["ShipCountry"],data["OrderID"],))
    conn.commit()
    #return the user
    updated_user = get_Order_by_id(data["OrderID"])
    return updated_user
# if __name__ == '__main__':

=======
import sqlite3
import csv
from tabnanny import check
from flask import Flask, request, jsonify

def connect_to_db():
    conn = sqlite3.connect('Northwind.db')
    return conn

# Operation on Product Table
def insert_Orders(data):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''INSERT INTO Orders (OrderID,CustomerID,EmployeeID,OrderDate,RequiredDate,ShippedDate,ShipVia,Freight,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry
) VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?,?,?,?,?)''', 
               (data["OrderID"],data["CustomerID"],data["EmployeeID"],
               data["OrderDate"],
            data["RequiredDate"],data["ShippedDate"],data["ShipVia"],data["Freight"],
            data["ShipName"],data["ShipAddress"],data["ShipCity"],data["ShipRegion"],
            data["ShipPostalCode"],data["ShipCountry"]))
        
    conn.commit()
    return {"Orders": "Inserted"}
def get_Orders():
    output = []
   
    conn = connect_to_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    all_orders = cur.fetchall()
    # convert row objects to dictionary
    for row in all_orders:
        data={}
        data["OrderID"]=row["OrderID"]
        data["CustomerID"]=row["CustomerID"]
        data["EmployeeID"]=row["EmployeeID"]
        data["OrderDate"]=row["OrderDate"]
        data["RequiredDate"]=row["RequiredDate"]
        data["ShippedDate"]=row["ShippedDate"]
        data["ShipVia"]=row["ShipVia"]
        data["Freight"]=row["Freight"]
        data["ShipName"]=row["ShipName"]
        data["ShipAddress"]=row["ShipAddress"]
        data["ShipCity"]=row["ShipCity"]
        data["ShipRegion"]=row["ShipRegion"]
        data["ShipPostalCode"]=row["ShipPostalCode"]
        data["ShipCountry"]=row["ShipCountry"]
        output.append(data)
    # print(output)
    return output
def get_Order_by_id(OrderID):
    data={}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Orders WHERE OrderID = ?", 
                       (OrderID,))
        row = cur.fetchone()
        # convert row object to dictionary
        if not row:
           return jsonify({'messsage': 'no customer found'})
        else:
            data["OrderID"]=row["OrderID"]
            data["CustomerID"]=row["CustomerID"]
            data["EmployeeID"]=row["EmployeeID"]
            data["OrderDate"]=row["OrderDate"]
            data["RequiredDate"]=row["RequiredDate"]
            data["ShippedDate"]=row["ShippedDate"]
            data["ShipVia"]=row["ShipVia"]
            data["Freight"]=row["Freight"]
            data["ShipName"]=row["ShipName"]
            data["ShipAddress"]=row["ShipAddress"]
            data["ShipCity"]=row["ShipCity"]
            data["ShipRegion"]=row["ShipRegion"]
            data["ShipPostalCode"]=row["ShipPostalCode"]
            data["ShipCountry"]=row["ShipCountry"]
    except:
        data={}
   
    return data
def update_Order(data):
    updated_user = {}
    
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('''UPDATE Orders SET CustomerID=?,EmployeeID=?,OrderDate=?,RequiredDate=?,ShippedDate=?,ShipVia=?,Freight=?,ShipName=?,ShipAddress=?,ShipCity=?,ShipRegion=?,ShipPostalCode=?,ShipCountry=? WHERE OrderID =?''',  
                    (data["CustomerID"],
                    data["EmployeeID"],data["OrderDate"],
            data["RequiredDate"],data["ShippedDate"],data["ShipVia"],data["Freight"],
            data["ShipName"],data["ShipAddress"],data["ShipCity"],data["ShipRegion"],
            data["ShipPostalCode"],data["ShipCountry"],data["OrderID"],))
    conn.commit()
    #return the user
    updated_user = get_Order_by_id(data["OrderID"])
    return updated_user
# if __name__ == '__main__':

>>>>>>> faecfc5bd35e0c9e68f76409f8510f35eb5885e9
