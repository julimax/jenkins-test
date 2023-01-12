pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }

           }
        stage('Copy Build') {
            steps {
                sh 'mkdir /var/lib/jenkins/jobs/buildCopy'
                sh 'cp /var/lib/jenkins/jobs/test/* /var/lib/jenkins/jobs/buildCopy'
            }
            
            
        }
    }
}