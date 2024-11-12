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
            echo 'Building sistema pedidos...'
            steps {
                dir('sistema_pedidos/src/main/java') {
                    // Compilar los archivos Java en `classes`
                    bat 'javac -d . classes/*.java'
                    // Ejecutar la clase `Main` con el nombre de paquete completo
                    bat 'java classes.Main'
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
