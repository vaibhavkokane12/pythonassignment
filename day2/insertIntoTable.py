from createDatabase import conn

name=input('Enter name:')
email=input('Enter email:')
phone=int(input('Enter phone:'))
query='INSERT INTO students(name,email,phone) VALUES(?,?,?)'
conn.execute(query,(name,email,phone))
conn.commit()
print('Record inserted successfully')