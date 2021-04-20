pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m main.py user_details.py'
                sh 'python --version'
            }
        }
    }
}
}