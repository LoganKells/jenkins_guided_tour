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
    // We can run with credentials for git repo
    withCredentials([gitUsernamePassword(credentialsId: 'github_logankells', gitToolName: 'Default')]) {
        sh 'git pull'
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