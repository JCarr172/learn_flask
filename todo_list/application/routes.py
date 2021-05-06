from application import app, db
from application.models import Tasks
from flask import render_template, request, redirect, url_for
from application.forms import TaskForm


@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    return render_template('home.html', title = 'Home', all_tasks = all_tasks)

@app.route('/add', methods=["GET","POST"])
def add():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Tasks(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html", title='Creation', form = form)

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    tasks_string =""
    for task in all_tasks:
        tasks_string += f"<br> {task.id} {task.description} {task.complete}"
    return tasks_string

@app.route('/delete/<number>', methods=["GET","POST"])
def delete(number):
    task = Tasks.query.filter_by(id=number).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/update/<number>', methods=['GET','POST'])
def update(number):
    form = TaskForm()
    task = Tasks.query.filter_by(id = number).first()
    if request.method == 'POST':
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", form=form, title='Update', task=task)

@app.route('/complete/<number>', methods=['Get','POST'])
def complete(number):
    form = TaskForm()
    task = Tasks.query.filter_by(id = number).first()
    task.complete = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/incomplete/<number>')
def incomplete(number):
    task = Tasks.query.filter_by(id = number).first()
    task.complete = False
    db.session.commit()
    return redirect(url_for("home"))