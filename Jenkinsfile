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
                bat 'python -m unittest API_tests_on_GamePower_and_UI_tests_on_YouTube/tests/api_test/api_test.py'
                bat 'python -m unittest API_tests_on_GamePower_and_UI_tests_on_YouTube/tests/ui_test/youtube_home_page_tests.py'

            }
        }
        stage('parallel') {
            steps {
                echo 'parallel..'
                bat 'python -m unittest API_tests_on_GamePower_and_UI_tests_on_YouTube/tests/ui_test/run_all_tests.py'

            }
        }
    }
}