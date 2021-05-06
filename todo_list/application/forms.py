from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField('Description of task', validators = [DataRequired()])
    submit = SubmitField('Add task')


