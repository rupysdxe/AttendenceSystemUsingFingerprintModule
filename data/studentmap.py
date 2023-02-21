import sqlite3


def insert_map(idd, name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO map VALUES (?, ?)", (idd, name))
    conn.commit()
    conn.close()

def get_map():
    d = dict()
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("Select * from map")
    arr = c.fetchall()
    for row in arr:
        d[row[0]] = row[1]
    conn.commit()
    conn.close()
    return d


