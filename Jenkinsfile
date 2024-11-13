pipeline {
    agent any

    environment {
        DESKTOP_PATH = 'C:\\Users\\camib\\Desktop'
    }

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
                    // Compilar los archivos Java en `classes`
                    bat 'javac -d . classes/*.java'
                    // Crear documentación Javadoc en la carpeta `docs`
                    bat 'javadoc -d docs classes/Main.java'
                    // Ejecutar la clase `Main` con el nombre de paquete completo
                    bat 'java classes.Main'
                }
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts allowEmptyArchive: true, artifacts: 'trivia/src/trivia.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'traductor_usql/src/traductor.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'sistema_pedidos/src/main/java/docs/*'
        
                // Copiar los archivos al escritorio
                bat 'copy "trivia/src/trivia.html" "C:\\Users\\camib\\Desktop\\trivia.html"'
                bat 'copy "traductor_usql/src/traductor.html" "C:\\Users\\camib\\Desktop\\traductor.html"'
                bat 'xcopy "sistema_pedidos/src/main/java/docs" "C:\\Users\\camib\\Desktop\\docs" /E /I'
            }
        }

        
    }
}

