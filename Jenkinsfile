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
    stage('Deploy') {
      agent any
      steps {
        echo 'Deploying....'
        input(message: 'ceshi', submitter: 'ces', submitterParameter: '12', id: '123', ok: 'ces')
      }
    }
  }
}