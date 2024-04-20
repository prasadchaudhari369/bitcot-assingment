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
                    docker.image("${imageName}:v${BUILD_NUMBER}").run("-p 5000:5000")
                }
            }
        }
        // stage ('install aws cli in server1') {
        //     steps {
        //         sshagent(credentials: ['34.207.99.5']) {
        //             sh 'apt install unzip -y'
        //             sh 'curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"'
        //             sh 'unzip awscliv2.zip'
        //             sh './aws/install'
        //             sh 'aws --version'
        //             sh 'usr/local/bin/aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 992382811051.dkr.ecr.us-east-1.amazonaws.com'
        //             sh 'docker run -it 992382811051.dkr.ecr.us-east-1.amazonaws.com/flaskapp:v1${BUILD_NUMBER}'
        //             sh 'docker run -it -p 992382811051.dkr.ecr.us-east-1.amazonaws.com/flaskapp:v1${BUILD_NUMBER}'
        //         }
        //     }
        // }
    }
}
