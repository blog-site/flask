from __main__ import app
from flask import Flask,request,Response
import json

@app.post("/auth/login")
def login():
    data=request.json
    return {
        "username": data['username']
    }
    
