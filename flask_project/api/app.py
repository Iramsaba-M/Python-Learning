# let's import the flask
import datetime
from flask import Flask,  Response, jsonify, request
import json
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib
from bson.objectid import ObjectId

# Your credentials (Replace with actual credentials)
username = "root"
password = "root@1234"

# Encode the username and password
encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)

uri = f"mongodb+srv://{encoded_username}:{encoded_password}@training-cluster.f8tfi.mongodb.net/?retryWrites=true&w=majority&appName=training-cluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.student_data

app = Flask(__name__)

# @app.route('/api/students', methods = ['GET'])
# def students ():
#     student_list = [
#         {
#             'name':'Asabeneh',
#             'country':'Finland',
#             'city':'Helsinki',
#             'skills':['HTML', 'CSS','JavaScript','Python']
#         },
#         {
#             'name':'David',
#             'country':'UK',
#             'city':'London',
#             'skills':['Python','MongoDB']
#         },
#         {
#             'name':'John',
#             'country':'Sweden',
#             'city':'Stockholm',
#             'skills':['Java','C#']
#         }
#     ]
#     return Response(json.dumps(student_list), mimetype='application/json')

@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    students = db.students.find()

    # Convert cursor to a list of dictionaries and ObjectId to string
    student_list = [{**student, '_id': str(student['_id'])} for student in students]

    return jsonify(student_list)

@app.route('/api/v1.0/students/<student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = db.students.find_one({'_id': ObjectId(student_id)})
    if student:
        student['_id'] = str(student['_id'])
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404

@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    try:
        # Parse JSON data
        data = request.get_json()

        # Debugging: Print received JSON data
        print("Received Data:", data)

        # Process data
        student_data = {
            'name': data['name'],
            'country': data['country'],
            'city': data['city'],
            'birthyear': int(data['birthyear']),
            'skills': data['skills'] if isinstance(data['skills'], list) else data['skills'].split(', '),
            'bio': data['bio'],
            'created_at': datetime.datetime.now()
        }

        # Insert into MongoDB (Ensure `db.students` is properly set up)
        db.students.insert_one(student_data)

        return jsonify(student_data), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    try:
        # Parse JSON data
        data = request.get_json()

        # Debugging: Print received JSON data
        print("Received Data:", data)

        # Process data
        student_data = {
            'name': data.get('name'),
            'country': data.get('country'),
            'city': data.get('city'),
            'birthyear': int(data.get('birthyear')) if data.get('birthyear') else None,
            'skills': data.get('skills') if isinstance(data.get('skills'), list) else data.get('skills', '').split(', '),
            'bio': data.get('bio')
        }

        # Update in MongoDB (Ensure `db.students` is properly set up)
        result = db.students.update_one({'_id': ObjectId(id)}, {'$set': student_data})

        if result.matched_count == 1:
            return jsonify(student_data), 200
        else:
            return jsonify({'error': 'Student not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    result = db.students.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'Student deleted successfully'}), 200
    else:
        return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)