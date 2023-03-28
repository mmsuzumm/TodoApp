'''Run this server with command "python main.py"
   Flask is working on port 5000
'''
from flask import Flask
from flask import request
from flask_cors import CORS
from connector import todos_records, todo_writer, todo_deleter, todo_delete_all
import json
app = Flask(__name__)
CORS(app)

@app.route("/todos")
def todos() -> json:
    data = todos_records()
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/todo_insert", methods=['POST'])
def todo_insert() -> json:
    received_json = json.loads(request.data.decode('utf8'))
    is_completed = received_json['isComplited']
    todo_text = received_json['todoText']
    data = todo_writer(is_completed, todo_text)
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

# @app.route("/todo_update", methods=['PUT'])
# def todo_update() -> None:
#     received_json = json.loads(request.data.decode('utf8'))
#     is_completed = received_json['isComplited']
#     todo_text = received_json['todoText']
#     print(todo_text, is_completed)
#     return 'OK'

@app.route("/todo_delete", methods=['DELETE'])
def todo_delete() -> json:
    received_json = json.loads(request.data.decode('utf8'))
    index = received_json['id']
    data = todo_deleter(index)
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/todo_clear", methods=['DELETE'])
def todo_clear() -> str:
    data = todo_delete_all()
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response 



if __name__ =='__main__':
    app.run()