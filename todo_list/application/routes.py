from application import app, db
from application.models import Tasks


@app.route('/')
@app.route('/home')
def hello_internet():
    return "This is the home page"

@app.route('/add')
def add():
    new_task = Tasks()
    db.session.add(new_task)
    db.session.commit()
    return "Task has been added"

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    tasks_string =""
    for task in all_tasks:
        tasks_string += f"<br> {task.id} {task.description} {task.complete}"
    return tasks_string

@app.route('/complete/<number>')
def complete(number):
    task = Tasks.query.filter_by(id = number).first()
    task.complete = True
    db.session.commit()
    return "Task completed"

@app.route('/incomplete/<number>')
def incomplete(number):
    task = Tasks.query.filter_by(id = number).first()
    task.complete = False
    db.session.commit()
    return "Task incomplete"

@app.route('/update/<number>/<descrip>')
def update(number,descrip):
    task = Tasks.query.filter_by(id = number).first()
    task.description = descrip
    db.session.commit()
    return "Description updated"