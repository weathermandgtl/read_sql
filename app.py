import mysql.connector
from flask import Flask
from flask_restful import Resource, Api, reqparse
import os

# db = mysql.connector.connect(host="localhost", user="root", password="skilover1!", database="testdatabase")
db = mysql.connector.connect(
    host=os.getenv('MYSQLHOST'),
    user=os.getenv('MYSQLUSER'),
    port=os.getenv('MYSQLPORT'),
    password=os.getenv('MYSQLPASSWORD'),
    database=os.getenv('MYSQLDATABASE'))

app = Flask("Test")
api = Api(app)
parser = reqparse.RequestParser()
# parser.add_argument('title', required=True, location='form')

class Test(Resource):
    def get(self):
        cursor = db.cursor()
        cursor.execute('SELECT * FROM GridTest WHERE id=1')
        record = cursor.fetchone()
        db.commit()
        db.close()
        return str(record)


api.add_resource(Test, '/')

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8080)




