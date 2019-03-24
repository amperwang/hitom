from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    phoneNum = db.Column(db.String(11), nullable = False, unique = True)
    userName = db.Column(db.String(16), nullable = False)
    course = db.Column(db.String(10), nullable = False)
    Number = db.Column(db.Integer, nullable = False)

@app.route('/yike')
def index():
    return render_template('index.html')

@app.route('/info', methods = ['POST'])
def addInfo():
    ntfInfo = {'result' : 'error'}
    if request.method == 'POST':
        data = request.get_json()
        phoneNum = data.get('phoneNum')
        userName = data.get('userName')
        course = data.get('course')
        Number = data.get('Number')

        if None != phoneNum and None != userName and None != course and None != Number:
            if Student.query.filter_by(phoneNum = phoneNum).first() == None:
                student = Student(phoneNum = phoneNum, userName = userName, course = course, Number = Number)
                db.session.add(student)
                db.session.commit()
                ntfInfo['result'] = 'success'
            else:
                ntfInfo['result'] = 'already_exist'

        return jsonify(ntfInfo)

if __name__ == '__main__':

    app.debug = True
    app.run()
