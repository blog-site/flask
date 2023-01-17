from mysql import connector

class SQL():
    def __init__(self):
        try:
            with open('/run/secrets/mysql_password','r') as f:
                user_passwd=f.read()
            self.db=connector.connect(
                host="mysql",
                user="db_user",
                password=user_passwd,
                port=3306
            )
        except Exception as e:
            print(e,flush=True)
            exit(1)
        return