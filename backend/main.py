'''Run this server with command "python main.py"
   Flask is working on port 5000
'''

from flask import Flask
from connector import todos_records
import json
app = Flask(__name__)

@app.route("/todos")
def todos():
    data = todos_records()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ =='__main__':
    app.run()