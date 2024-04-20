pipeline {
    agent any 
    environment {
        registryCreds = 'ecr:us-east-1:awscreds'
        imageName = '992382811051.dkr.ecr.us-east-1.amazonaws.com/flaskapp'
        registryUrl = 'https://992382811051.dkr.ecr.us-east-1.amazonaws.com'
    }

    stages {
        stage('Fetch Code from GitHub') {
            steps {
                git branch: 'main', credentialsId: 'github-creds', url: "https://github.com/prasadchaudhari369/bitcot-assingment.git"
            }
        }

        stage('Build docker image'){
            steps {
                script {
                    dockerImage = docker.build(imageName+":v${BUILD_NUMBER}", ".")
                }
            }
        }

        stage('Upload the image on ECR') {
            steps{
                script{
                    docker.withRegistry(registryUrl, registryCreds) {
                        dockerImage.push("v1${BUILD_NUMBER}")
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("${imageName}:v${BUILD_NUMBER}").run("-p 80:80")
                }
            }
        }
    }
}
