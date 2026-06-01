import os
from flask import Flask, redirect, url_for
from config import Config
from models import db, Teacher
from routes import teachers_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(teachers_bp)

    @app.route('/')
    def index():
        return redirect(url_for('teachers.list_teachers'))

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
