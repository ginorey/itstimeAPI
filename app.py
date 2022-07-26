#!/user/bin/env python
# encoding: utf-8

import json
from flask import Flask, jsonify, request


app = Flask(__name__)
@app.route('/allfighters', methods=['GET'])
def all_fighters():
    with open('data/fighter_info.json', 'r') as f:
        temp = f.read()
        data = json.loads(temp)
    return data

@app.route('/ID', methods=['GET'])
def search_id():
    requested_ID = request.args.get('ID')
    print(requested_ID)
    with open('data/fighter_info.json', 'r') as f:
        temp = f.read()
        data = json.loads(temp)
        for rows in data:
            if rows['ID'] == requested_ID:
                return jsonify(rows)
            else:
                return jsonify({'error': 'ID was not found.'})
        
app.route('/name', methods=['GET'])
def search_name():
    requested_name = request.args.get('name')
    print(requested_name)
    with open('data/fighter_info.json', 'r') as f:
        temp = f.read()
        data = json.loads(temp)


app.run()