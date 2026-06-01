from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Teacher

teachers_bp = Blueprint('teachers', __name__, url_prefix='/teachers')

@teachers_bp.route('/')
def list_teachers():
    all_teachers = Teacher.query.order_by(Teacher.name).all()
    return render_template('index.html', teachers=all_teachers, title='All Teachers')

@teachers_bp.route('/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        phone = request.form.get('phone', '').strip()
        hire_date_str = request.form.get('hire_date', '').strip()

        if not all([name, email, subject, hire_date_str]):
            flash('Name, email, subject, and hire date are required.', 'danger')
            return render_template('add_teacher.html', title='Add Teacher')

        try:
            hire_date = datetime.strptime(hire_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD.', 'danger')
            return render_template('add_teacher.html', title='Add Teacher')

        existing = Teacher.query.filter_by(email=email).first()
        if existing:
            flash('A teacher with this email already exists.', 'danger')
            return render_template('add_teacher.html', title='Add Teacher')

        teacher = Teacher(name=name, email=email, subject=subject, phone=phone, hire_date=hire_date)
        db.session.add(teacher)
        db.session.commit()
        flash('Teacher added successfully!', 'success')
        return redirect(url_for('teachers.list_teachers'))

    return render_template('add_teacher.html', title='Add Teacher')

@teachers_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_teacher(id):
    teacher = Teacher.query.get_or_404(id)

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        phone = request.form.get('phone', '').strip()
        hire_date_str = request.form.get('hire_date', '').strip()

        if not all([name, email, subject, hire_date_str]):
            flash('Name, email, subject, and hire date are required.', 'danger')
            return render_template('edit_teacher.html', teacher=teacher, title='Edit Teacher')

        try:
            hire_date = datetime.strptime(hire_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD.', 'danger')
            return render_template('edit_teacher.html', teacher=teacher, title='Edit Teacher')

        if email != teacher.email:
            existing = Teacher.query.filter_by(email=email).first()
            if existing:
                flash('A teacher with this email already exists.', 'danger')
                return render_template('edit_teacher.html', teacher=teacher, title='Edit Teacher')

        teacher.name = name
        teacher.email = email
        teacher.subject = subject
        teacher.phone = phone
        teacher.hire_date = hire_date
        db.session.commit()
        flash('Teacher updated successfully!', 'success')
        return redirect(url_for('teachers.list_teachers'))

    return render_template('edit_teacher.html', teacher=teacher, title='Edit Teacher')

@teachers_bp.route('/delete/<int:id>', methods=['POST'])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    flash('Teacher deleted successfully!', 'success')
    return redirect(url_for('teachers.list_teachers'))
