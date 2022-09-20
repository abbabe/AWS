from flask_sqlalchemy import SQLAlchemy
 
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
        
 
    def __repr__(self):
        return f"{self.name}:{self.surname}"