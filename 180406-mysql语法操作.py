
import pymysql


db = pymysql.connect("192.168.11.101","root","111111","test")
scursor = db.cursor()

#sql = "insert into Student (name,age) values ('CC',27)"

#sql = "delete from Student"

sql = "select * from Student"

try:
    scursor.execute(sql)
    #db.commit()
except:
    pass
    #db.rollback()


#data = scursor.fetchone()
data = scursor.fetchall()
print(data)

scursor.close()
db.close()