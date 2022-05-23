pipeline {
    agent any
    parameters {
        string(name: "EMAIL_RECIPIENTS", defaultValue: "Test", trim: true, description: "Sample string parameter")
        string(name: "Email_sender", defaultValue: "Test", trim: true, description: "Sample string parameter")
        text(name: "Email_Message", defaultValue: "Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET", description: "Sample multi-line text parameter")
        string(name: "Email configurations", defaultValue: "Test", trim: true, description: "Sample string parameter")
    }
    stages {
        stage("Email Notification") {
            steps {
                   sh 'python3 -u MonitoringTest/Jenkinsfile $EMAIL_RECIPIENTS' 
            }
        }
    }
}
