from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt
from functools import wraps
import os
from dotenv import load_load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
# Enable CORS for your React frontend
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})  # Update with your Vite dev server port

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')  # Use environment variable in production
app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)

# Error handling
class APIError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code

@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({'error': error.message})
    response.status_code = error.status_code
    return response

# JWT token verification decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            raise APIError('Token is missing', 401)
        
        try:
            token = token.split(' ')[1]  # Remove 'Bearer ' prefix
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data  # You would typically query your database here
        except jwt.ExpiredSignatureError:
            raise APIError('Token has expired', 401)
        except jwt.InvalidTokenError:
            raise APIError('Invalid token', 401)
            
        return f(current_user, *args, **kwargs)
    return decorated

# Routes
@app.route('/api/debate', methods=['POST'])
@token_required
def create_debate(current_user):
    try:
        data = request.get_json()
        
        if not data:
            raise APIError('No JSON data provided')
        
        required_fields = ['title', 'description', 'userStances']
        if not all(field in data for field in required_fields):
            raise APIError('Missing required fields')
        
        # Validate data types
        if not isinstance(data['title'], str) or not isinstance(data['description'], str):
            raise APIError('Invalid data types for title or description')
        
        if not isinstance(data['userStances'], list):
            raise APIError('userStances must be an array')
            
        # Here you would typically save to a database
        # For now, we'll just echo back the data
        response = {
            "message": "Debate created successfully",
            "debate": {
                "id": "generated-id",  # You would generate this when saving to DB
                "title": data['title'],
                "description": data['description'],
                "userStances": data['userStances'],
                "createdBy": current_user['id'],
                "createdAt": datetime.utcnow().isoformat()
            }
        }
        
        return jsonify(response), 201

    except Exception as e:
        raise APIError(str(e))

@app.route('/api/debate/<debate_id>', methods=['GET'])
@token_required
def get_debate(current_user, debate_id):
    # Here you would typically fetch from a database
    # This is just an example response
    debate = {
        "id": debate_id,
        "title": "Example Debate",
        "description": "Example Description",
        "userStances": [],
        "createdBy": "user-id",
        "createdAt": datetime.utcnow().isoformat()
    }
    
    return jsonify(debate), 200

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        raise APIError('Missing email or password')
        
    # Here you would verify against your database
    # This is just an example
    if data['email'] == 'test@example.com' and data['password'] == 'password':
        token = jwt.encode({
            'id': 'user-id',
            'email': data['email'],
            'exp': datetime.utcnow() + app.config['JWT_EXPIRATION_DELTA']
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token}), 200
    
    raise APIError('Invalid credentials', 401)

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true')