pipeline {
    agent any 

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/<YourUsername>/<RollNo-ISA2>.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t <roll_no> .'
                }
            }
        }

        stage('Cleanup Existing Container') {
            steps {
                script {
                    sh 'docker rm -f <roll_no> || true'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d --name <roll_no> -p 5000:5000 <roll_no>'
                }
            }
        }
    }
}
