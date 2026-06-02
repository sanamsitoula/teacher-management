pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = '1'
        PATH = "/var/jenkins_home/.local/bin:/usr/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'pip3 install flake8 && flake8 app.py models.py routes.py config.py --max-line-length=120 || true'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t teacher-management:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'sudo docker compose -f docker-compose.yml down && sudo docker compose -f docker-compose.yml up -d'
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
