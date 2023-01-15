pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 source/date.py > date.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 source/test.py > test.txt'
            }

           }
        stage('Copy Build') {
            steps {
                sh 'mkdir -p /var/lib/jenkins/jobs/buildCopy'
                sh 'cp -rf /var/lib/jenkins/jobs/test/* /var/lib/jenkins/jobs/buildCopy'
            }
            
            
        }
    }
}