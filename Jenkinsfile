// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent {
        docker { image 'python:3' }
    }
    stages {
//         stage ('pull_from_scm') {
//             steps {
//                 // We can run with credentials for git repo
//                 withCredentials([gitUsernamePassword(credentialsId: 'github_logankells', gitToolName: 'Default')]) {
//                     sh 'git pull'
//                 }
//             }
//         }
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