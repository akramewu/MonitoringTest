pipeline {
    agent any
    parameters {
        string(name: "Email recipients", defaultValue: "Test", trim: true, description: "Sample string parameter")
        text(name: "TEST_TEXT", defaultValue: "Jenkins Pipeline Test", description: "Sample multi-line text parameter")
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
