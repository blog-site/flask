from __main__ import app
from flask import Flask,request,Response,jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"]="cidCfqisLr5d+HlW+CpXx4RYAe4="  # Change this!
jwt=JWTManager(app)

@app.post("/auth/login")
def login():
    data=request.json
    username=data.get("username", None)
    password=data.get("password", None)
    if username!="user1" or password != "abc123":
        return jsonify({"msg": "Bad username or password"}),401
    access_token=create_access_token(identity=username)
    return jsonify(access_token=access_token)
