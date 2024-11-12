pipeline {
    agent any

    stages {

        stage('Correr Trivia - Python') {
            steps {
                dir('trivia/src') {
                    echo 'Building trivia...'
                    bat 'python3 -m pydoc -w trivia'
                    bat 'dir'
                }    
            }
        }

         stage('Correr USQL - Python') {
            steps {
                dir('traductor_usql/src') {
                    echo 'Building traductor USQL...'
                    bat 'python3 -m pydoc -w traductor'
                    bat 'dir'
                }    
            }
        }

        stage('Correr Pedidos - Java') {
            steps {
                echo 'Building sistema pedidos...'
                dir('sistema_pedidos/src/main/java') {
                    bat 'javac classes/*.java'
                    bat 'java classes.Main'
                    bat 'javadoc -d docs Main.java'
                    bat 'dir'
                }
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts allowEmptyArchive: true, artifacts: 'trivia/src/trivia.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'traductor_usql/src/traductor.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'sistema_pedidos/main/java/classes/docs/Main.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'sistema_pedidos/main/java/classes/docs/*'
            }
        }
        
    }
}
