pipeline {
    agent {
        docker { image 'cturra/ntp' }
    }
    stages {
        stage('Building') {
            steps {
                 echo 'Building...'
                 sh 'docker run --name=ntp            \
              			  --restart=always      \
              			  --detach              \
                                --publish=123:123/udp \
              			    cturra/ntp'
            }
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'docker exec ntp chronyc tracking'
            }
        }
    }
}