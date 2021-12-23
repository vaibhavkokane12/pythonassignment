from createDatabase import conn

query='ALTER TABLE students ADD COLUMN marks INT NOT NULL DEFAULT 0'
conn.execute(query)
print('Table modified successfully')