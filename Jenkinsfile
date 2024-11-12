pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/pazdiaz15/programacion_avanzada.git', branch: 'main'
            }
        }
     
        stage('PyDoc Traductor USQL') {
            steps {
                    sh 'python3 -m pydoc -w traductor_usql/src/traductor'
                    sh 'ls -l'
                }
            }
        
        stage('PyDoc Trivia') {
             steps {
                     sh 'python3 -m pydoc -w trivia/src/trivia'
                     sh 'ls -l'
                 }
         }

        stage('Archive') {
            steps {
                archiveArtifacts allowEmptyArchive: true, artifacts: 'trivia/src/trivia.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'traductor_usql/src/traductor.html'
            }
        }
    }
}
