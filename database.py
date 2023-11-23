import sqlite3 as sql

conn = sql.connect('lifeForm.db', check_same_thread=False)

c = conn.cursor()

##c.execute("""
##    CREATE TABLE lifeForm (
##        domain TEXT,
##        kingdom TEXT,
##        family TEXT,
##        species TEXT,
##        description TEXT,
##        image TEXT
##    )
##""")
