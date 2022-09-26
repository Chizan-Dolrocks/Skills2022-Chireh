pipeline {
    agent {
        docker {
            image 'cturra/ntp'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker run --name=ntp            \
                               --restart=always      \
              		       --detach              \
              			 --publish=123:123/udp \
              			 cturra/ntp'
            }
        }
    }
}