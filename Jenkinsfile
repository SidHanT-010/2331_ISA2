pipeline {
    agent any
          stages {
                stage('Build Docker Image') {
                                                    steps {
                                                          script {
                                                          dockerImage = docker.build("sidhant10/Docker-Images-via-Jenkins")
                                                                  }
                                                            }
                                                      }
                  stage('Run Docker Container') {
          steps {
                              script {
                                dockerImage.run('-d -p 7070:8080')
                                      }
                              }
                    }
              }
          }
