pipeline {
    agent any

    stages {

        stage('Correr Trivia - Python') {
            steps {
                dir('trivia/src') {
                    sh 'python3 -m pip install -r requirements.txt'
                    echo 'Building trivia...'
                    sh 'python3 -m pydoc -w trivia'
                    sh 'ls -l'
                }    
            }
        }

         stage('Correr USQL - Python') {
            steps {
                dir('traductor_usql/src') {
                    sh 'python3 -m pip install -r requirements.txt'
                    echo 'Building USQL...'
                    sh 'python3 -m pydoc -w traductor'
                    sh 'ls -l'
                }    
            }
        }

        stage('Correr Pedidos - Java') {
            steps {
                echo 'Building...'
                dir('sistema_pedidos/main/java/classes') {
                    sh 'javac Order.java OrderProcessing.java Packaging.java Payment.java Shipping.java'
                    sh 'javac Main.java'
                    sh 'java Main'
                    sh 'javadoc -d docs Main.java'
                    sh 'ls -l'
                }
            }
        }

        stage('Archive') {
            steps {
                // Archivar el archivo trivia.html como artefacto
                archiveArtifacts allowEmptyArchive: true, artifacts: 'trivia/src/trivia.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'traductor_usql/src/traductor.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'sistema_pedidos/src/docs/Main.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'sistema_pedidos/src/docs/*'
            }
        }
        
    }
}
