import sqlite3

conn=sqlite3.connect('todoapp.db')
print('database opened successfully')
create_table='''CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_title VARCHAR(255),
                task_details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''
conn.execute(create_table)
print('tasks table created successfully')
conn.close()