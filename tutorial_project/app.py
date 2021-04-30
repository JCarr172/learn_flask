import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#use for stand alone database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

#use for in built database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def hello_internet():
    return "Hello Internet!"

@app.route('/nextpage')
def next_page():
    return "This is a new page!!"

@app.route('/squared/<int:number>')
def squared(number):
    return f"This is your number squared {number**2}"


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
    