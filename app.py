from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

USER_ID = "kalyan_chakravarthy"
COLLEGE_EMAIL = "kalyan.chakravarthy2021@vitstudent.ac.in"
COLLEGE_ROLL_NUMBER = "21BAI1759"

@app.route('/process', methods=['POST'])
def process_request():
    if request.method == 'POST':
        data = request.get_json()
        
        # Extracting input array from the request
        input_array = data.get('data', [])

        # Separating numbers and alphabets
        numbers = [str(x) for x in input_array if isinstance(x, int)]
        alphabets = [str(x) for x in input_array if isinstance(x, str) and x.isalpha()]
        
        # Finding the highest lowercase alphabet
        lowercase_alphabets = [x for x in alphabets if x.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

        # Creating the response
        response = {
            'is_success': True,
            'user_id': USER_ID,
            'email': COLLEGE_EMAIL,
            'roll_number': COLLEGE_ROLL_NUMBER,
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_lowercase_alphabet': [highest_lowercase] if highest_lowercase else []
        }

        return jsonify(response)

    elif request.method == 'GET':
        return jsonify({'operation_code': 'OPERATION_1234'})

if __name__ == '__main__':
    app.run(debug=True)
