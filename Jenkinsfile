pipeline {
    agent any
    parameters {
        string(name: "Email_Recipients", defaultValue: "Test", trim: true, description: "Sample string parameter")
        string(name: "Email_sender", defaultValue: "Test", trim: true, description: "Sample string parameter")
        text(name: "Email_Message", defaultValue: "Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET", description: "Sample multi-line text parameter")
        string(name: "Email configurations", defaultValue: "Test", trim: true, description: "Sample string parameter")
    }
    stages {
        stage("Email Notification") {
            steps {
                script{
                   sh 'python3 -u demoemail.py' 
                }
                echo "Build stage."
                echo "Hello $params.Email_Recipients"
            }
        }
    }
}
