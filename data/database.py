import bcrypt
import sqlite3


def insert(username, password):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    password = password.encode('utf-16')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    c.execute("INSERT INTO admins VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()


def isAdmin(username, password):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    password = password.encode('utf-16')
    c.execute("SELECT password FROM admins WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()
    if row is not None:
        stored_password = row[0]
        if bcrypt.checkpw(password, stored_password):
            return True
    return False



