from datetime import date
from run import app, db
from models import Teacher

sample_teachers = [
    {"name": "Alice Johnson", "email": "alice@school.com", "subject": "Mathematics", "phone": "111-222-3333", "hire_date": date(2023, 8, 15)},
    {"name": "Bob Williams", "email": "bob@school.com", "subject": "Physics", "phone": "222-333-4444", "hire_date": date(2022, 9, 1)},
    {"name": "Carol Davis", "email": "carol@school.com", "subject": "Chemistry", "phone": "333-444-5555", "hire_date": date(2024, 1, 10)},
    {"name": "David Brown", "email": "david@school.com", "subject": "English", "phone": "444-555-6666", "hire_date": date(2023, 3, 22)},
    {"name": "Eva Martinez", "email": "eva@school.com", "subject": "History", "phone": "555-666-7777", "hire_date": date(2022, 11, 5)},
]

with app.app_context():
    db.create_all()
    for data in sample_teachers:
        exists = Teacher.query.filter_by(email=data["email"]).first()
        if not exists:
            teacher = Teacher(**data)
            db.session.add(teacher)
    db.session.commit()
    count = Teacher.query.count()
    print(f"Seeded {count} teachers.")
