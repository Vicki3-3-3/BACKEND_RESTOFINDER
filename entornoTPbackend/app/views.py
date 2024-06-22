from flask import jsonify

def index():
    return jsonify({'message':'Hello World API Restofinder'})