// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python:3.9.7 } }
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
                sh 'echo "Hello World"'
                sh ''' echo "Multiline shell steps work :)"
                '''
            }
        }
    }
}