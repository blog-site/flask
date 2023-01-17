from __main__ import app

from flask import jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity

@app.get('/file/<int:fid>')
@jwt_required()
def get_file(fid:int):
    current_user=get_jwt_identity()
    return jsonify(logged_in_as=current_user),200