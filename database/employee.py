import sqlite3


def employee(D):
    data = {
        "EmpId":  D[0], 
        "Name":  D[1], 
        "Title":  D[2], 
        "PhoneNo":  D[3]
    }

    return data


def InsertEmp(EmpId, Name, Title, PhoneNo):
     with sqlite3.connect("clothingStoredb.db") as conn:
          handler = conn.cursor()
          query = handler.execute( """ insert into Employees (EmpId,Name,Title,PhoneNo)   values('{}','{}','{}','{}') """.format(EmpId, Name, Title, PhoneNo))
          conn.commit()

def getEmp():
     with sqlite3.connect("clothingStoredb.db") as conn:
          handler = conn.cursor()
          query = handler.execute( """ select * from Employees where EmpId=83  """)
          person = query.fetchone()
          print(person)

def updateEmp():
     with sqlite3.connect("clothingStoredb.db") as conn:
          handler = conn.cursor()
          query = handler.execute( """UPDATE employees set Name='bobby' where EmpId=83  """)
          


def getAllEmp():
     with sqlite3.connect("clothingStoredb.db") as conn:
          handler = conn.cursor()
          query = handler.execute( """ select * from Employees """)
          person = query.fetchall()
          print(person)


def deleteEmp():
     with sqlite3.connect("clothingStoredb.db") as conn:
          handler = conn.cursor()
          query = handler.execute( """DELETE from employees where EmpId=83""")
        


deleteEmp()
# print(InsertEmp(
#      "83",
#      "sswds",
#      "saseass",
#      "44444",
#      )
#       )                   
   
  