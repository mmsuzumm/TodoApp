'''Run this server with command "python main.py"
   Flask is working on port 5000
'''
from flask import Flask
from flask import request
from flask_cors import CORS
from connector import db_operation_todos
import json
app = Flask(__name__)
CORS(app)

@app.route("/todos")
def todos() -> json:
    data = db_operation_todos(operation_type='select_all')
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/todo_create", methods=['POST'])
def todo_create() -> json:
    received_json = json.loads(request.data.decode('utf8'))
    is_completed = received_json['isCompleted']
    todo_text = received_json['todoText']
    data = db_operation_todos(operation_type='new_todo', is_completed=is_completed, todo_text=todo_text)
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/todo_update_status", methods=['PATCH'])
def todo_update_status() -> str:
    received_json = json.loads(request.data.decode('utf8'))
    id = received_json['id']
    is_completed = received_json['isCompleted']
    data = db_operation_todos(operation_type='update_status', id=id, is_completed=is_completed)
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response 


@app.route("/todo_delete", methods=['DELETE'])
def todo_delete() -> app.response_class:
    received_json = json.loads(request.data.decode('utf8'))
    id = received_json['id']
    db_operation_todos('delete', id=[id,])  #id passed like list so in db user method ANY() 
    response = app.response_class(
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/todo_clear", methods=['DELETE'])
def todo_clear() -> str:
    data = db_operation_todos('delete_all')
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response 

if __name__ =='__main__':
    app.run()