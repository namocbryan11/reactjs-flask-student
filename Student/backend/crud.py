from flask import Flask, request, jsonify, json, redirect, url_for, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS
from werkzeug.exceptions import RequestEntityTooLarge

app = Flask(__name__)

cors = CORS(app)

app.config['MYSQL_HOST'] = 'localhost';
app.config['MYSQL_USER'] = 'root';
app.config['MYSQL_PASSWORD'] = 'bryan123';
app.config['MYSQL_DB'] = 'practice1';

mysql = MySQL(app)


@app.route("/getStudents", methods=['GET'])
def students(): 
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    students = cur.fetchall()
    return {"students": students};

@app.route("/addStudent", methods=['POST'])
def addStudents():
    student = json.loads(request.data)
    firstname = student["firstname"]
    lastname = student["lastname"]
    course = student["course"]
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO student(Firstname,Lastname,Course) VALUES" +
    "(%s,%s,%s)", (firstname,lastname,course))
    mysql.connection.commit()
    res = {'status':'ok'}
    return res

if __name__ == "__main__":
    app.run(debug=True)