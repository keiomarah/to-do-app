from flask import render_template, Blueprint, request, jsonify, redirect, url_for
from .models import Task
from flask_login import login_required, current_user
from . import db
from datetime import datetime
import json

views = Blueprint('views', __name__, template_folder='.templates')

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

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

    return redirect(url_for('views.home'), user=current_user)

@views.route('/update-task', methods=['POST'])
@login_required
def update_task():
    taskId = json.loads(request.data)['taskId']

    task = Task.query.filter_by(id=taskId).first()
    if task:
        task.complete = not task.complete
        db.session.commit()
    return jsonify({})