node {
    stage('Checkout') {
       git branch: 'pipeline', credentialsId: 'alfred_github', url: 'https://github.com/cogniwide/cognidocs-core.git'
   }

        stage('download-model'){
        }

      stage ('Docker build'){
            docker.build('cognidiscovery-core')
      }
  }
