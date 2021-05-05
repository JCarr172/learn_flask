from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, BooleanField, DateField
import os
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET')

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Age')
    date = DateField('Date')
    email = BooleanField('Emails')
    class_ = SelectField('Class', choices = ['Wizard', 'Fighter', 'Rogue', 'Cleric'])
    submit = SubmitField('Add Name')

class UserCheck:
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            message = 'Please choose another username'
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

class Bannedchar:
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            message = 'Included special characters'
        self.message = message

    def __call__(self, form, field):
        for char in field.data:
            if char in self.banned:
                raise ValidationError(self.message)
            

class myForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.
        UserCheck(message="custom rejection message",banned = ['root','admin','sys']),
        Bannedchar(banned = ['%','*','+',' ','?']),
        Length(min=2,max=15)
        ])
    submit = SubmitField('Sign up')



@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/b_names')
def b_names():
    names = ["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template('b_names.html',names = names)

@app.route('/', methods=['GET','POST'])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('user.html', form = form, username=username)
    else:
        return render_template('user.html', form = form, username="")


@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return f'Thank you {first_name} {last_name}'

    return render_template('home.html', form=form, message=error)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")