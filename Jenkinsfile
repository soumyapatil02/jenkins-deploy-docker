pipeline {
    agent any

    environment {
        IMAGE_NAME = 'employee-management-api'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements-dev.txt
                    python -m pytest -q
                '''
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }
    }
}
