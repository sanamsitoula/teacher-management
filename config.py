import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://teacher_user:teacher_pass@localhost:3306/teacher_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
