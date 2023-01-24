from __main__ import app,sql
from flask import Flask,request,Response,jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

from bcrypt import gensalt,hashpw,checkpw

with open('/run/secrets/jwt_secret_key','r') as f:
    app.config["JWT_SECRET_KEY"]=f.read()
jwt=JWTManager(app)

@app.post("/auth/login")
def login():
    data=request.json
    username=data.get("username", None)
    password=data.get("password", None)
    if sql.checkName(username)==False:
        return jsonify(msg="Bad username or password"),401
    if not checkpw(password.encode(),sql.getPassword(username).encode()):
        return jsonify(msg="Bad username or password"),401
    access_token=create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.post("/auth/register")
def register():
    data=request.json
    username=data.get("username",None)
    password=data.get("password",None)
    print(username,password,flush=True)
    if sql.checkName(username):
        return jsonify(msg=f"Username '{username}' conflicted"),409
    hashed=hashpw(password.encode(),gensalt())
    sql.createUser(username,hashed)
    return jsonify(msg="OK"),200
