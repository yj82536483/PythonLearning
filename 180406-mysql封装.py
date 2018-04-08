import pymysql

class packMysql():
    def __init__(self,host,user,password,dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname

    def connect(self):
        self.db = pymysql.connect(self.host,self.user,self.password,self.dbname)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
        except:
            print("查询失败")
        finally:
            self.close()

        return res


    def get_all(self,sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except:
            print("查询失败")
        finally:
            self.close()

        return res

if __name__ == "__main__":
        p = packMysql("192.168.11.101","root","111111","test")
        r = p.get_all("select * from Student")
        print(r)