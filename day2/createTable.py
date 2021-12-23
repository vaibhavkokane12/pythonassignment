from createDatabase import conn

query='''CREATE TABLE students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        phone BIGINT NOT NULL)
    '''
conn.execute(query)
print('Table created successfully')