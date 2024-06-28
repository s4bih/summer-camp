from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "ABC987"
db = SQLAlchemy(app)


#create a tabel
class students(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   Name = db.Column(db.String(100))
   Age = db.Column(db.String(100))
   DOB = db.Column(db.String(100))
   Gender = db.Column(db.String(100))


   def __init__(self,name, age, dob, gender):
       self.Name = name
       self.Age = age
       self.DOB = dob
       self.Gender = gender




@app.route('/', methods=['GET', 'POST'])
def add_students():
   if request.method == 'POST':
       name = request.form['name']
       age = request.form['age']
       dob = request.form['dob']
       gender = request.form['gender']
       student = students(name, age, dob, gender)
       db.session.add(student)
       db.session.commit()
       print("sent")

       return redirect(url_for('detail'))


   return render_template('student.html')


@app.route('/detail')
def detail():
   all_student = students.query.all()
   return render_template('detail.html', students=all_student)


if __name__ == '__main__':
   app.run(debug=True)