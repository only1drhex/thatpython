import sqlite3

connect = sqlite3.connect("comp.db")
a = connect.cursor()

'''
a.execute(
    """
create Table employees(
        EmpId integer,
        FirstNAme text,
        LastName text,
      
)

"""
)
'''

a.execute("INSERT INTO employees VALUES(1, 'Kenny', 'mark', 244)") 

a.execute("INSERT INTO employees VALUES(3, 'fendi', 'james', 233)") 
a.execute("INSERT INTO employees VALUES(3, 'rende', 'dean', 233)") 
# delete from the table
a.execute("UPDATE employees set LastName='bobby' where EmpId=1 ")
# a.execute("DELETE from employees set LastName='bobby' where EmpId=1 ")

for i in range(4):
    print(a.fetchone())





connect.commit()