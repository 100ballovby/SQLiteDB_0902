import sqlite3


class Database:
    def __init__(self, db, tn='table'):
        self.table_name = tn
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table_name} 
            (id INTEGER PRIMARY KEY,
            hostname TEXT,
            brand TEXT,
            ram INTEGER,
            flash INTEGER
            )"""
        )
        self.conn.commit()

    def fetch(self, hostame=''):
        self.cur.execute(
            f"""SELECT * FROM {self.table_name} 
            WHERE hostname LIKE '%{hostame}%'"""
        )
        rows = self.cur.fetchall()
        return rows

