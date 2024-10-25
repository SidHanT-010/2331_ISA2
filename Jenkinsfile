pipeline {
    agent any 

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/SidHanT-010/2331_ISA2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t sidhant10/2331_isa2 .'
                }
            }
        }

        stage('Build and Run Docker Container') {
            steps {
                script {
                    
                    bat "docker rm -f my-app-container || exit 0"

                    
                    bat "docker run -d --name my-app-container sidhant10/2331_isa2"
                }
            }
        }
    }
}
