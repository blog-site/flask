from flask import Flask
from sql import SQL

app=Flask(__name__)
sql=SQL()

import routers.auth 
import routers.user
import routers.file

@app.route("/test")
def test():
    return "Hello, world!\n"

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000,ssl_context=('/run/secrets/cert','/run/secrets/privkey'))
