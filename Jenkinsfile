pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'pip install flake8 && flake8 app.py models.py routes.py config.py --max-line-length=120'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t teacher-management:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose down && docker-compose up -d'
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed! Check logs.'
        }
        success {
            echo 'Teacher Management app deployed successfully!'
        }
    }
}
