# let's import the flask
# from flask import Flask, render_template
# import os

# import pymongo # importing operating system module
# MONGODB_URI = 'mongodb+srv://root:root@1234@training-cluster.f8tfi.mongodb.net/?retryWrites=true&w=majority&appName=training-cluster'
# client = pymongo.MongoClient(MONGODB_URI)
# print(client.list_database_names())

# app = Flask(__name__)
# if __name__ == '__main__':
#     # for deployment we use the environ
#     # to make it work for both production and development
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)



#
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

# students = [
#         {'name':'David','country':'UK','city':'London','age':34},
#         {'name':'John','country':'Sweden','city':'Stockholm','age':28},
#         {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
#     ]
# for student in students:
#     db.students.insert_one(student)

# student = db.students.find_one()
# print(student)

student = db.students.find_one({'_id' : ObjectId('67c18ef518599724bd62a462')})
print(student)

# students = db.students.find()
# for student in students:
#     print(student)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print(client.list_database_names())
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)