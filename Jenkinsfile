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
                    bat 'dir' // Verifica que trivia.html se genera
                }    
            }
        }

        stage('Correr USQL - Python') {
            steps {
                dir('traductor_usql/src') {
                    echo 'Building traductor USQL...'
                    bat 'python3 -m pydoc -w traductor'
                    bat 'dir' // Verifica que traductor.html se genera
                }    
            }
        }

        stage('Correr Pedidos - Java') {
            steps {
                echo 'Building sistema pedidos...'
                dir('sistema_pedidos/src/main/java') {
                    bat 'javac -d . classes/*.java'
                    bat 'javadoc -d docs classes/Main.java'
                    bat 'dir docs' // Verifica que la carpeta docs se genera correctamente
                }
            }
        }

        stage('Archive') {
            steps {
                // Archivar en Jenkins
                archiveArtifacts allowEmptyArchive: true, artifacts: 'trivia/src/trivia.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'traductor_usql/src/traductor.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'sistema_pedidos/src/main/java/docs/*'

                // Copiar archivos al escritorio, verificando si existen
                bat 'if exist "trivia/src/trivia.html" copy "trivia/src/trivia.html" "%DESKTOP_PATH%\\trivia.html"'
                bat 'if exist "traductor_usql/src/traductor.html" copy "traductor_usql/src/traductor.html" "%DESKTOP_PATH%\\traductor.html"'
                bat 'if exist "sistema_pedidos/src/main/java/docs" xcopy "sistema_pedidos/src/main/java/docs" "%DESKTOP_PATH%\\docs" /E /I'
            }
        }
    }
}


