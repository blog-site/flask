from flask import Flask

app=Flask(__name__)

import routers.auth 

@app.route("/test")
def test():
    return "Hello, world!\n"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
