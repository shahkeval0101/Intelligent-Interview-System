import sqlite3 as sql

con = sql.connect("data.db")

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
