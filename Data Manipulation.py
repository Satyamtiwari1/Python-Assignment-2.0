import mysql.connector
import json
import re
import numpy as np
import pandas as pd
pd.options.display.max_columns = None


class DB:
    def __init__(self) -> None: 
        # Connecting to the server
        self.conn = mysql.connector.connect(host='localhost',
                    port='3306',
                    user='root',
                    password='satyam',
                    database='employees')
        self.cur = self.conn.cursor()
    # Create Table with Columns
    def create_tables(self):
        self.cur.execute("Create table json_to_sql_table (name varchar(100),phone varchar(100),email varchar(100),address varchar(100),region varchar(100),country varchar(100),list int,postalzip varchar(200),currency varchar(100));")
        self.conn.commit()
    #Load or Insert Data From JSON File to MySQL
    def load_data(self):
        with open('data.json','r',encoding='utf-8') as rf:
            data = json.load(rf)
        for row in data["data"]:
            self.cur.execute("insert into json_to_sql_table values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
            self.conn.commit()
    #Load Data to PANDAS DataFrame
    def load_to_pandas(self):
        self.cur.execute("select * from json_to_sql_table;")
        rows = self.cur.fetchall()
        self.df = pd.DataFrame(rows,columns=["name","phone","email","address","region","country","list","postalZip","currency"])
    # Show data in from of PANDAS DataFrame
    def show_data(self):
        print(self.df.head())
    # Change Email
    def Email(self,email):
            new_email = email.split('@')[0] + "@gmail.com"
            return new_email
    def Change_Email(self):
        self.df["email"]=self.df["email"].apply(self.Email)
        print(self.df.head())
        
    # Change Postal Code
    def change_postal_code(self):
        self.df["postalZip"]=self.df["postalZip"].str.replace('[^0-9]',"")
        self.df["postalZip"]=self.df["postalZip"].astype(np.int64)
        print(self.df)
      
    # Change Phone Number To ASCII
    def convert_phone(self,phone_no):
        phone_no = re.sub("[^0-9]+","",phone_no)
        return_string = ''
        for i in range(0,len(phone_no),2):
            try:
                temp_no = int(phone_no[i]+phone_no[i+1])
            except IndexError:
                return return_string
            if temp_no < 65:
                return_string += "O"
            else:
                return_string += chr(temp_no)

        return return_string

    def modify_phone_no(self):
        self.df["phone"]=self.df["phone"].apply(self.convert_phone)
        print(self.df)
            

        

if __name__ == '__main__':
    D = DB()
    # D.create_tables()
    # D.load_data()
    D.load_to_pandas()
    D.show_data()
    D.Change_Email()
    D.change_postal_code()
    D.modify_phone_no()