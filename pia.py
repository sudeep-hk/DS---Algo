from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple REST API endpoint that returns a list of colors
@app.route('/colors', methods=['GET'])
def get_colors():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    return jsonify(colors)

# A REST API endpoint that accepts POST requests with JSON payloads
# and returns the sum of the two numbers in the payload
@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
