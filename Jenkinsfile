pipeline {
    agent any

    environment {
        // Define your Image names here so you only have to change them in one place
        DOCKER_HUB_USER = 'yjawlekar'
        BACKEND_IMAGE   = 'audio-analyzer-backend'
        FRONTEND_IMAGE  = 'audio-analyzer-frontend'
        }
    stages {
        stage ("build") {
            steps {
                sh "docker build -t ${DOCKER_HUB_USER}/${BACKEND_IMAGE}:latest ./backend"
                sh "docker build -t ${DOCKER_HUB_USER}/${FRONTEND_IMAGE}:latest ./frontend"
            }
        }

        stage ("push") {
            // OPEN THE VAULT
                steps{
                    withcredentials([usernamepassword(credentialsId: 'docker_hub_creds',
                                                                    usernameVariable: 'USER',
                                                                    passwordVariable: 'PASS')]) {
                   // 1. LOGIN using the variables from the vault
                        sh "echo ${PASS}| docker login -u ${USER} --password-stdin"
                         // 2. PUSH using your environment variables
                        sh "docker push ${DOCKER_HUB_USER}/${BACKEND_IMAGE}:latest"
                        sh "docker push ${DOCKER_HUB_USER}/${FRONTEND_IMAGE}:latest"
                                                    }
                        }                            
                    }



        stage ("deploy") {
            steps {
            sh "docker-compose pull && docker-compose up"
            }
        }
    }
}
