import sqlite3
from sqlite3 import Error


def create_db(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(sqlite3.version)
        return connection
    except Error as e:
        print(e)
    return connection


def create_table(conn, table):
    try:
        c = conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)


def main():
    db = 'test.db'
    sql_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY,
    name text NOT NULL,
    begin_date text,
    end_date text
    );"""
    sql_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY,
    name text NOT NULL,
    priority integer,
    status_id integer NOT NULL,
    project_id integer NOT NULL,
    begin_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

    conn = create_db(db)
    if conn is not None:
        create_table(conn, sql_projects_table)
        create_table(conn, sql_tasks_table)
    else:
        print('Error! cannot create connection')


def create_project(conn, project):
    sql = """
    INSERT INTO projects(name,begin_date,end_date)
    VALUES(?,?,?)
    """
    cursor = conn.cursor()
    cursor.execute(sql, project)
    conn.commit()
    return cursor.lastrowid


def create_task(conn, task):
    sql = """
        INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
        VALUES(?,?,?,?,?,?)
        """
    cursor = conn.cursor()
    cursor.execute(sql, task)
    conn.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    db = 'test.db'
    connection = create_db(db)
    with connection:
        project = ('Cool App with sqlite', '2021-02-09', '2021-02-21')
        project_id = create_project(connection, project)

        task_1 = ('Analyze dependencies', 1, 1, project_id, '2021-02-09', '2021-02-12')
        task_2 = ('Confirm with user', 1, 1, project_id, '2021-02-13', '2021-02-15')

        create_task(connection, task_1)
        create_task(connection, task_2)