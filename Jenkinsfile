pipeline {
    agent any

    stages {

        stage('Correr Trivia - Python') {
            steps {
                dir('trivia/src') {
                    bat 'python3 -m pip install -r requirements.txt'
                    echo 'Building trivia...'
                    bat 'python3 -m pydoc -w trivia'
                    bat 'ls -l'
                }    
            }
        }

         stage('Correr USQL - Python') {
            steps {
                dir('traductor_usql/src') {
                    bat 'python3 -m pip install -r requirements.txt'
                    echo 'Building USQL...'
                    bat 'python3 -m pydoc -w traductor'
                    bat 'ls -l'
                }    
            }
        }

        stage('Correr Pedidos - Java') {
            steps {
                echo 'Building...'
                dir('sistema_pedidos/main/java/classes') {
                    bat 'javac Order.java OrderProcessing.java Packaging.java Payment.java Shipping.java'
                    bat 'javac Main.java'
                    bat 'java Main'
                    bat 'javadoc -d docs Main.java'
                    bat 'ls -l'
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
