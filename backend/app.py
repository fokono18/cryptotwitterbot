from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for your Vite frontend
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api', methods=['POST'])
def handle_debate():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
            

       
            
        # Validate userStances structure
        
        
        # Process the debate details
        response = {
            "message": "Debate details received",
            "debate": {
                "title": data['title'],
                "description": data['description'],
                "userStances": data['userStances']
            }
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)