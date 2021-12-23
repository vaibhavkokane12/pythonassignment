from createDatabase import conn

query='SELECT * FROM students'
cursor=conn.execute(query)
print('Table records are:\n')
for row in cursor:
    print('id:',row[0])
    print('name:',row[1])
    print('email:',row[2])
    print('phone:',row[3])
    print()