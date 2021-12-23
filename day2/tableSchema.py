from createDatabase import conn

query='SELECT sql FROM sqlite_master WHERE name="students"'
cursor=conn.execute(query)
for row in cursor:
    print("Table schema is:\n",row[0])