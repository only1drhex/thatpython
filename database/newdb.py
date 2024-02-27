import sqlite3
connect = sqlite3.connect("execs.db")
a = connect.cursor()
# a.execute(
#     """ 
#     CREATE TABLE executives(
#         ID integer,
#         Name text
#     )
#     """
# )

# a.execute("INSERT INTO executives VALUES(1, 'jack morGAN')")
a.execute("SELECT * FROM executives ")

print(a.fetchone())

connect.commit()
# bANK
# STORE
# ENTTITTES RELATIIONSHIP ATTR
