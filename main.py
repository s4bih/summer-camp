from flask import Flask,request,render_template,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'ABC!$123'
db=SQLAlchemy(app)


class student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(100))
    age = db.Column(db.String(100))
    DOB = db.Column(db.String(100))
    gender = db.Column(db.String(100))













@app.route('/',methods=['GET','POST'])
def add_student():
    return render_template('student.html')

if __name__ == '__main__':
    app.run(debug=True)