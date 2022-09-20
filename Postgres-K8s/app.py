from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
#from models import db, EmployeeModel



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@db.c4qk1p7b0xwv.us-east-1.rds.amazonaws.com/dagicloud'



db =SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "employees"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    surname = db.Column(db.String())
    age= db.Column(db.String())
    email = db.Column(db.String())
 
 
    def __init__(self, name,surname,email,age):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        






@app.route('/')
def index():
  
     return render_template('index.html')   



@app.route('/submit', methods=['POST'])
def submit():
  name= request.form['name']
  surname=request.form['surname']
  age=request.form['age']
  email=request.form['email']
 
  employee=EmployeeModel(name,surname,age,email)
  db.session.add(employee)
  db.session.commit()
 
  #fetch a certain employee
  employeeResult=db.session.query(EmployeeModel).filter(EmployeeModel.id==1)
  for result in employeeResult:
    print(result.name)
 
  return render_template('success.html', data=name)





if __name__ == '__main__':
    app.run(debug=True,port=80)