pipeline {
    agent any 

    stages {
        stage('Clone Repository') {
            steps {
                git https://github.com/SidHanT-010/2331_ISA2.git
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t sidhant10/2331_isa2 .'
                }
            }
        }

        stage('Cleanup Existing Container') {
            steps {
                script {
                    sh 'docker rm -f sidhant10/2331_isa2 || true'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d --name sidhant10/2331_isa2 -p 5000:5000 sidhant10/2331_isa2'
                }
            }
        }
    }
}
