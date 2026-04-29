from flask import render_template, Blueprint, request
from .models import Task
from flask_login import login_required, current_user
from . import db
from datetime import datetime

views = Blueprint('views', __name__, template_folder='.templates')

@views.route('/')
@login_required
def home():
    return render_template('home.html')

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

    return render_template('home.html', user=current_user)