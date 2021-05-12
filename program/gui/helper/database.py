import sqlite3 as sql
import os

local_path = os.path.realpath(__file__)
parent_path = os.path.dirname(os.path.realpath(__file__))
# print(local_path)
print(parent_path)
filename = os.path.join(str(parent_path),"resources", "data.db")
print(filename)

con = sql.connect(filename)

cur = con.cursor()

# cur.execute("""
# CREATE TABLE IF NOT EXISTS "users" (
#     "username"  TEXT,
#     "password"  TEXT
# );

# """)

# cur.execute("""
# INSERT INTO "users" VALUES ('boss','1234');
# """)

# cur.execute("""
# INSERT INTO "users" VALUES ('admin','password');
# """)

# cur.execute("""
# INSERT INTO "users" VALUES ('Kevalshah90909@gmail.com','keval123');
# """)


cur.execute("""SELECT username, password FROM users""")


print(cur.fetchall())

con.commit()
con.close()
