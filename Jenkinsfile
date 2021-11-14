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
        stage('dependencies') {
            steps {
                sh 'ls'
                sh 'python3 -m venv ./venv'
                sh 'ls ./venv'
//                 sh """
//                     python3 -m venv ./venv
//                     source ./venv/bin/activate
//                     python3 -m pip install -r requirements.txt
//                     """
            }
        }
        stage('build') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('test') {
            steps {
                sh 'pytest ./test/test_math.py --junitxml=test_report.xml'
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