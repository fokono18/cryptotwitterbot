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
            
        # Validate the structure matches DebateDetails
        if not all(field in data for field in ['title', 'description', 'userStances']):
            return jsonify({"error": "Missing required fields"}), 400
            
        # Validate userStances structure
        for stance in data['userStances']:
            required_stance_fields = ['username', 'confidence', 'argument', 'stance']
            if not all(field in stance for field in required_stance_fields):
                return jsonify({"error": "Invalid UserStance structure"}), 400
        
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