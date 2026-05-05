from flask import render_template, Blueprint, request, jsonify, redirect, url_for
from .models import Task
from flask_login import login_required, current_user
from . import db
from datetime import datetime
import json
from datetime import date

views = Blueprint('views', __name__, template_folder='.templates')

@views.route('/')
@login_required
def home():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    today = date.today()

    for task in tasks:
       task.is_today = task.due == today
    return render_template('home.html', user=current_user)

@views.route("/all-tasks")
@login_required
def all_tasks():
    return render_template('all-tasks.html', user=current_user)

@views.route("/completed-tasks")
@login_required
def completed_tasks():
    return render_template("completed.html", user=current_user)

@views.route("/high-priority-tasks")
@login_required
def high_priority_tasks():
    return render_template("high-priority.html", user=current_user)

@views.route('/add-task', methods=['POST'])
@login_required
def add_task():
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        due_date = datetime.strptime(request.form.get('due_date'), "%Y-%m-%d").date()
        priority = request.form.get('priority')

        new_task = Task(task_name=task_name, due=due_date, priority=priority, user_id=current_user.id)

        db.session.add(new_task)
        db.session.commit()

    return redirect(request.referrer)

@views.route('/update-task', methods=['POST'])
@login_required
def update_task():
    taskId = json.loads(request.data)['taskId']

    task = Task.query.get(taskId)
    if task:
        task.complete = not task.complete
        db.session.commit()
    return jsonify({})

@views.route('delete-task', methods=['POST'])
@login_required
def delete_task():
    taskId = json.loads(request.data)['taskId']

    task = db.session.get(Task, taskId)
    print(task)
    if task: 
        db.session.delete(task)
        db.session.commit()
    return jsonify({})

@views.route('/tasks', methods=['GET'])
def tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).all()

    return jsonify([
    {
        "id": task.id,
        "title": task.task_name,
        "completed": task.complete,
        "due": task.due.isoformat()
    }
    for task in tasks
    ])
