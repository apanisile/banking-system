pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m main2.py'
                sh 'python --version'
            }
        }
    }
}
}