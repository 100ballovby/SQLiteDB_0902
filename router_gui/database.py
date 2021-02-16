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

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, hostname, brand, ram, flash):
        self.cur.execute(f"""
        INSERT INTO {self.table_name} 
        VALUES (NULL, {hostname}, {brand}, {ram}, {flash})
        """)
        self.conn.commit()

    def remove(self, id):
        self.cur.execute(f"""
        DELETE FROM {self.table_name} WHERE id = {id}
        """)
        self.conn.commit()

    def update(self, id, hostname, brand, ram, flash):
        self.conn.execute(f"""
        UPDATE {self.table_name} SET hostname={hostname}, 
        brand={brand}, ram={ram}, flash={flash} WHERE id={id}
        """)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
