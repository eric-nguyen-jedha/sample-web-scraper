pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                script {
                    deleteDir() // nettoie le workspace avant le clone
                }
                git branch: 'development',
                    url: 'https://github.com/eric-nguyen-jedha/sample-web-scraper.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('simple-scraper:latest')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image('simple-scraper:latest').inside {
                        sh 'pytest tests/tests.py --junitxml=results.xml'
                    }
                }
            }
        }
        stage('Archive Results') {
            steps {
                junit 'results.xml'
            }
        }
    }
    post {
        success {
            script {
                echo "Success"
                emailext(
                    subject: "Jenkins Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """<p>Good news!</p>
                             <p>The build <b>${env.JOB_NAME} #${env.BUILD_NUMBER}</b> was successful.</p>
                             <p>View the details <a href="${env.BUILD_URL}">here</a>.</p>""",
                    to: 'enguyen.fr@gmail.com'
                )
            }
        }
        failure {
            script {
                echo "Failure"
                emailext(
                    subject: "Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """<p>Unfortunately, the build <b>${env.JOB_NAME} #${env.BUILD_NUMBER}</b> has failed.</p>
                             <p>Please check the logs and address the issues.</p>
                             <p>View the details <a href="${env.BUILD_URL}">here</a>.</p>""",
                    to: 'enguyen.fr@gmail.com@jedha.co'
                )
            }
        }
    }
}
