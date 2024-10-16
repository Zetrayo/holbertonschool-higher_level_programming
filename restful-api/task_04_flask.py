#!/usr/bin/python3
"""ye"""


from flask import Flask, jsonify, request


app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}


@app.route('/')
def home():
    """ye"""
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_usernames():
    """ye"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status', methods=['GET'])
def status():
    """ye"""
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """ye"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """ye"""
    data = request.get_json()
    username = data.get("username")
    if (not username or not data.get("name") or not
            data.get("age") or not data.get("city")):
        return jsonify({"error": "Missing required fields"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added successfully",
                    "user": users[username]}), 201
