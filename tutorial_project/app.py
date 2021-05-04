import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#use for stand alone database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
# use form 'msql+pymysql://user:password@Public IP/database name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#use for in built database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    orders = db.relationship('Orders', backref='customer') 

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float)
    orders = db.relationship('Orders', backref='product') 

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('products.id'))

class Army(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    army_name = db.Column('Army name', db.String(30), nullable=False)
    faction = db.Column('Army faction', db.String(30), nullable=False)
    alignment = db.Column('Alignment', db.String(30), nullable=False)

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Integer, nullable=False)
# @app.route('/')
# @app.route('/home')
# def hello_internet():
#     return "Hello Internet!"

# @app.route('/nextpage')
# def next_page():
#     return "This is a new page!!"

# @app.route('/squared/<int:number>')
# def squared(number):
#     return f"This is your number squared {number**2}"


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
    