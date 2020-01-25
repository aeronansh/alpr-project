import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="vehicle")

mycursor=conn.cursor()

mycursor.execute("""select * from vehicle_registration_sheet1 where Fuel='PETROL'""")

obr=mycursor.fetchall()

x=list(obr)

for i in x:
    print("Name: ",i[4],"License PLate: ",i[0],"\n")
    print("----------------------------------------")



