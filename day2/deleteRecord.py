from createDatabase import conn

id=int(input('Enter id to delete:'))
query="DELETE FROM students WHERE id=?"
conn.execute(query,(id,))
conn.commit()
print('Record deleted successfully')