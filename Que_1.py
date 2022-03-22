import mysql.connector as connector

con=connector.connect(host='localhost',
                    port='3306',
                    user='root',
                    password='satyam',
                    database='employees')

print(con)
print('Connection successfull')
def fetch():
    query="select * from employees"
    cur=con.cursor()
    cur.execute(query)
    for row in cur.fetchall():
         yield row       
# main
a=fetch()
# for fetching 10 records
for i in range(10):
    print(next(a))


