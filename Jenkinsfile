pipeline {
    agent any
    
    environment {
        // Define environment variables here
        DOCKER_HUB_CREDENTIALS = 'dockerhub_credentials' // Jenkins credentials ID for Docker Hub
        DOCKER_REGISTRY_URL = 'docker.io' // Docker Hub registry URL
        FRONTEND_IMAGE_NAME = 'techshack176/frontend-image-jenkins'
        BACKEND_IMAGE_NAME = 'techshack176/backend-image-jenkins'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                git 'https://github.com/techshack103/devops-scrapper-jenkins.git'
            }
        }
        
        stage('Build Frontend Docker Image') {
            steps {
                script {
                    // Build frontend Docker image
                    docker.build(FRONTEND_IMAGE_NAME, '-f client/Dockerfile client')
                }
            }
        }
        
        stage('Build Backend Docker Image') {
            steps {
                script {
                    // Build backend Docker image
                    docker.build(BACKEND_IMAGE_NAME, '-f client/Dockerfile .')
                }
            }
        }
        
        stage('Push Docker Images to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub
                    docker.withRegistry(DOCKER_REGISTRY_URL, DOCKER_HUB_CREDENTIALS) {
                        // Push frontend Docker image
                        docker.image(FRONTEND_IMAGE_NAME).push()
                        
                        // Push backend Docker image
                        docker.image(BACKEND_IMAGE_NAME).push()
                    }
                }
            }
        }
    }
}
