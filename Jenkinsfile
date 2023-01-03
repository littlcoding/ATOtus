pipeline {
  agent any
  stages {
     stage('Install deps') {
        steps {
            sh 'pip3 install -r requirements.txt '
        }
     }
     stage('Run tests') {
        steps {
            catchError {
                sh "python3 -m pytest ${TESTS_PATH} -n ${THREADS} --browser ${BROWSER} --bv ${BROWSER_VERSION} --executor ${EXECUTOR} --base_url ${OPENCART_URL}"
            }
        }
     }
     stage('Reports') {
        steps {
           allure([
               includeProperties: false,
               jdk: '',
               properties: [],
               reportBuildPolicy: 'ALWAYS',
               results: [[path: 'report']]
    	   ])
  	      }
       }
    }
}
