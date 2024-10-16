#!/usr/bin/python3
"""ye"""


from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "admin": {"password": generate_password_hash("adminpass"),
              "role": "admin"},
    "user1": {"password": generate_password_hash("user1pass"),
              "role": "user"}
}


@auth.verify_password
def verify_password(username, password):
    """ye"""
    if username in users and check_password_hash(users[username]
                                                 ["password"], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """ye"""
    return jsonify(
        {"message": f"Hello,
         {auth.current_user()}! You are accessing a protected route."})


@app.route('/login', methods=['POST'])
def login():
    """ye"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username not in users or not check_password_hash(users[username]
                                                        ['password'],
                                                        password):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity={"username": username,
                                                 "role": users[username]
                                                 ['role']})
    return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """ye"""
    current_user = get_jwt_identity()
    return jsonify(
        {"message": f"Hello,
         {current_user['username']}! This route is protected by JWT."})


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """ye"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": f"Hello,
                    {current_user['username']}! You are an admin."})
