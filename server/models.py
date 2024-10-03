from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer)

    def __repr__(self):
        return f'<Employee {self.id}, {self.name}, {self.salary}>'

# creating a model called department
class Department(db.Model):
    # creating a table called department
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)

    # creating a string representation of the db
    def __repr__(self):
        return f"<Department {self.id}, {self.name}, {self.address}>"
