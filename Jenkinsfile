pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "psn19/resume-website"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '📥 Pulling latest code from GitHub...'
                git branch: 'main', url: 'https://github.com/Prathamesh192/resume-website.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                echo '🔐 Logging into Docker Hub...'
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }

        stage('Push Docker Image') {
            steps {
                echo '🚀 Pushing Docker image to Docker Hub...'
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
    }

    post {
        success {
            echo '✅ CI/CD pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs for details.'
        }
    }
}
