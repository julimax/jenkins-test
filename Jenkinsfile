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
                sh 'python3 -m pylint source/date.py'
            }

           }
        stage('Copy Build') {
            steps {
                sh 'mkdir /var/lib/jenkins/jobs/buildCopy'
                sh 'cp -r /var/lib/jenkins/jobs/test/* /var/lib/jenkins/jobs/buildCopy'
            }
            
            
        }
    }
}