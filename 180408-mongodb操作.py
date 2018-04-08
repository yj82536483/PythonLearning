from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("localhost",27017)
db = conn.mydb
collection = db.student

#插入
#collection.insert({"name":"tom","age":20})

#查询
res = collection.find({"age":{"$gt":10}})
for row in res:
    print(type(row))
    print(row)

#统计查询
print(collection.find({"age":{"$gt":10}}).count())

#根据ID查询，需导入ObjectId库
res = collection.find({"_id":ObjectId("5ac9faa02b62789f3dcd2c64")})
print(res[0])

#排序
res = collection.find({"age":{"$gt":10}}).sort("age")

#分页
res = collection.find({"age":{"$gt":10}}).skip(1).limit(2).sort("age")
for row in res:
    #print(type(row))
    print(row)

#更新
collection.update({"name":"tom"},{"$set":{"age":25}})

#删除
collection.remove({"name":"tom"})

conn.close()