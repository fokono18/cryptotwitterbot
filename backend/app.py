from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_request():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    response = {
        "message": "Data received successfully",
        "received_data": data
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
