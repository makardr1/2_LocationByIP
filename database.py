import sqlite3


def base(data: tuple):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS location(
    Status TEXT,
    Country TEXT,
    Countrycode TEXT,
    Region TEXT,
    Regionname TEXT,
    City TEXT,
    Zip INT,
    Lat REAL,
    Lon REAL,
    Timezone TEXT,
    Isp TEXT,
    Org TEXT,
    Auto_system TEXT,
    Query TEXT);
    """)
    try:
        check = cur.execute(f"SELECT * FROM location WHERE Query=?", (data[-1],))
        if len(list(*check)) == 0:
            cur.execute("INSERT INTO location VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);", data)
            conn.commit()
        else:
            print("Duplicate")
    except TypeError:
        pass
