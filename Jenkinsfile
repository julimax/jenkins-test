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
                sh 'cd /var/lib/jenkins/jobs/test'
            }
            steps {
                sh 'mkdir buildCopy'  
            }
            steps {
                sh 'cp /var/lib/jenkins/jobs/test/* /var/lib/jenkins/jobs/buildCopy'
            }
            
        }
    }
}