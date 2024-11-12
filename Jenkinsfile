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
                    echo 'Building USQL...'
                    bat 'python3 -m pydoc -w traductor'
                    bat 'dir'
                }    
            }
        }

        stage('Correr Pedidos - Java') {
            steps {
                echo 'Building...'
                dir('sistema_pedidos/src/main/java/classes') {
                    bat 'javac Order.java OrderProcessing.java Packaging.java Payment.java Shipping.java'
                    bat 'javac Main.java'
                    bat 'java Main'
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
