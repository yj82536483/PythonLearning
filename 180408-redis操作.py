import redis

r = redis.StrictRedis(host="localhost",port=6379)

r.set("aaa","aaaaaaaa")

print(r.get("aaa"))

#缓冲多条数据
pipe = r.pipeline()
pipe.set("bb","bbb")
pipe.set("cc","cc")
pipe.execute()