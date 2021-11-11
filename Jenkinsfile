// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
            }
        }
    }
    post {
        always {
            echo 'Completed'
        }
        success {
            echo 'Successful completion.'
        }
        failure {
            echo 'Failed completion.'
        }
    }
}