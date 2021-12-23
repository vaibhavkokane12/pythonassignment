import sqlite3

conn=sqlite3.connect('todoapp.db',check_same_thread=False)

create_table='''CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_title VARCHAR(255),
                task_details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
conn.execute(create_table)