from time import sleep
from mysql import connector

class SQL():
    def __init__(self):
        try:
            with open('/run/secrets/mysql_root_password','r') as f:
                root_passwd=f.read().strip()
            self.db=connector.connect(
                host="mysql",
                user="root",
                password=root_passwd,
                port=3306,
                database="db"
            )
        except Exception as e:
            print(e,flush=True)
            sleep(3)
            exit(1)

    def createUser(self,username:str,password:str):
        cur=self.db.cursor()
        sql="INSERT INTO users (username,password) VALUES (%s,%s)"
        val=(username,password)
        cur.execute(sql,val)
        self.db.commit()
    def showUsers(self):
        cur=self.db.cursor()
        cur.execute("SELECT * FROM users")
        return cur.fetchall()
    def checkName(self,username:str)->bool:
        cur=self.db.cursor()
        sql="SELECT EXISTS(SELECT 1 FROM `users` WHERE `username`=%s)"
        val=(username,)
        cur.execute(sql,val)
        return cur.fetchone()[0]
    def getPassword(self,username:str):
        cur=self.db.cursor()
        sql="SELECT `password` FROM `users` WHERE `username`=%s"
        val=(username,)
        cur.execute(sql,val)
        return cur.fetchone()[0]
