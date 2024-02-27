# create a proram that will connect to a database stored in music.sqlite3 of the current directory if it doesnt exist create it and create a table called writers
import sqlite3
# create a sqlite3 connection object in this directory
connect = sqlite3.connect("music.sqlite3")
# create a cursor object

a = connect.cursor()


# a.execute(
#     """ 
#     CREATE TABLE writers(
#         ID integer,
#        Name text
#     )
#     """
# )
# insert a record into the table 1, jack london
a.execute("INSERT INTO writers VALUES(1, 'jack london')")
a.execute("INSERT INTO writers VALUES(2, 'Honore de Balzac')")
a.execute("INSERT INTO writers VALUES(3, 'Lion Feuchtwanger')")
a.execute("INSERT INTO writers VALUES(4, 'Emile Zola')")
a.execute("INSERT INTO writers VALUES(5, 'Truman Capote')")


connect.commit()