// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent {
        docker { image 'node:14-alpine' }
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