from flask import Flask, request, jsonify, g

app = Flask(__name__)

# Middleware
@app.before_request
def before_request():
    g.start_time = request.headers.get('X-Request-Start', 'No Start Time Provided')
    print(f"Before request: Start time - {g.start_time}")

@app.after_request
def after_request(response):
    response.headers['X-Custom-Header'] = 'This is a custom header'
    print("After request: Added custom header to response")
    return response

# Routes
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name', 'Guest')
    return f'Hello, {name}!'

@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(data)

@app.route('/update', methods=['PUT'])
def update():
    return 'This is a PUT request.'

@app.route('/delete', methods=['DELETE'])
def delete():
    return 'This is a DELETE request.'

# Error Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
