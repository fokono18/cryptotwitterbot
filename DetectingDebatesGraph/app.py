from flask import Flask, request, jsonify
from flask_cors import CORS
from main import main
import json

app = Flask(__name__)
# Enable CORS for your Vite frontend
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api', methods=['POST'])
def handle_debate():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
            

        # Process the debate details
        response = json.dumps(main())
        
        
        print(response)
        return response, 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)