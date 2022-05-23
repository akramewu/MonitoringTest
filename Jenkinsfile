pipeline {
    agent any
    parameters {
        string(name: "Email recipients", defaultValue: "Test", trim: true, description: "Sample string parameter")
        string(name: "Email sender", defaultValue: "Test", trim: true, description: "Sample string parameter")
        text(name: "Email message", defaultValue: "Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET", description: "Sample multi-line text parameter")
        string(name: "Email configurations", defaultValue: "Test", trim: true, description: "Sample string parameter")
    }
    stages {
        stage("Build") {
            steps {
                echo "Build stage."
                echo "Hello $params.TEST_STRING"
            }
        }
        stage("Test") {
            steps {
                echo "Test stage."
            }
        }
    }
}
