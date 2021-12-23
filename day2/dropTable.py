from createDatabase import conn

query='DROP TABLE students'
conn.execute(query)
print('Table droped successfully')