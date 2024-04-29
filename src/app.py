from flask import Flask,jsonify,request


app = Flask(__name__)

todos = [
   {"label":"Sample todo 1", "done": True },
   {"label":"Sample todo 2", "done": True }
];


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    return jsonify('Response for the POST todo')

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    return 'something'

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)












