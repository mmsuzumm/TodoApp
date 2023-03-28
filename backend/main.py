'''Run this server with command "python main.py"
   Flask is working on port 5000
'''
from flask import Flask
from flask import request
from flask_cors import CORS
from connector import todos_records, todo_writer, todo_deleter
import json
app = Flask(__name__)
CORS(app)

@app.route("/todos")
def todos():
    data = todos_records()
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/todo_insert", methods=['POST'])
def todo_insert() -> None:
    received_json = json.loads(request.data.decode('utf8'))
    is_completed = received_json['isComplited']
    todo_text = received_json['todoText']
    data = todo_writer(is_completed, todo_text)
    print(data)
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
def todo_delete() -> None:
    received_json = json.loads(request.data.decode('utf8'))
    index = received_json['id']
    data = todo_deleter(index)
    return data

if __name__ =='__main__':
    app.run()