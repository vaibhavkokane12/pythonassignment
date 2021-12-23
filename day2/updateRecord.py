from createDatabase import conn

id=int(input('Enter id to update:'))
name=input('Enter name:')
email=input('Enter email:')
phone=int(input('Enter phone:'))
query='UPDATE students SET name=?,email=?,phone=? WHERE id=?'
conn.execute(query,(name,email,phone,id))
conn.commit()
print('Record updated successfully')