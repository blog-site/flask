from __main__ import app,sql

from flask import jsonify
from flask import request

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

@app.put("/user")
@jwt_required()
def update():
    img=request.files.get('file',None)
    username=get_jwt_identity()
    sql.uploadAvator(username,img.read())
    return jsonify(msg="Avator uploaded"),201

@app.get("/user/<string:username>")
def get(username):
    img=sql.getAvator(username)
    return img,200
