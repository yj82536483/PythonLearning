import pymysql


db = pymysql.connect("192.168.11.101","root","111111","test")
scursor = db.cursor()

sql = "select * from Student"
scursor.execute(sql)

data = scursor.fetchone()

print(data)
scursor.close()
db.close()