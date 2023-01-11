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
                mkdir test2  
            }
            steps {
                cp /var/lib/jenkins/workspace/test/* /var/lib/jenkins/workspace/test2
            }
        }
    }
}