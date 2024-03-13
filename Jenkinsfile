// pipeline {
//     agent any
//     stages {
//         stage('Build') {
//             steps {
//                 echo 'Building..'
//             }
//         }
//         stage('Test') {
//             steps {
//                 echo 'Testing..'
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 echo 'Deploying..'
//             }
//         }
//     }
// }
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
//                 sh 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Add test execution steps here
                sh 'python -m unittest tests/api_test/api_test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
                git 'commit -am "Deploying latest changes"'
                git 'push origin main'

            }
        }
    }
}