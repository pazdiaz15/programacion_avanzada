pipeline {
    agent any

    environment {
        DESKTOP_PATH = 'C:\\Users\\camib\\Desktop'
        WORKSPACE_PATH = 'C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\work-test'
    }

    stages {

        stage('Correr Trivia - Python') {
            steps {
                dir("${WORKSPACE_PATH}\\trivia\\src") {
                    echo 'Building trivia...'
                    bat 'python3 -m pydoc -w trivia'
                    bat 'dir' 
                }    
            }
        }

        stage('Correr USQL - Python') {
            steps {
                dir("${WORKSPACE_PATH}\\traductor_usql\\src") {
                    echo 'Building traductor USQL...'
                    bat 'python3 -m pydoc -w traductor'
                    bat 'dir' 
                }    
            }
        }

        stage('Correr Pedidos - Java') {
            steps {
                echo 'Building sistema pedidos...'
                dir("${WORKSPACE_PATH}\\sistema_pedidos\\src\\main\\java") {
                    bat 'javac -d . classes/*.java'
                    bat 'javadoc -d docs classes/Main.java'
                    bat 'dir docs' 
                }
            }
        }

        stage('Archive') {
            steps {
               
                archiveArtifacts allowEmptyArchive: true, artifacts: "${WORKSPACE_PATH}\\trivia\\src\\trivia.html"
                archiveArtifacts allowEmptyArchive: true, artifacts: "${WORKSPACE_PATH}\\traductor_usql\\src\\traductor.html"
                archiveArtifacts allowEmptyArchive: true, artifacts: "${WORKSPACE_PATH}\\sistema_pedidos\\src\\main\\java\\docs\\*"

                
                bat "if exist \"${WORKSPACE_PATH}\\trivia\\src\\trivia.html\" copy \"${WORKSPACE_PATH}\\trivia\\src\\trivia.html\" \"%DESKTOP_PATH%\\trivia.html\""
                bat "if exist \"${WORKSPACE_PATH}\\traductor_usql\\src\\traductor.html\" copy \"${WORKSPACE_PATH}\\traductor_usql\\src\\traductor.html\" \"%DESKTOP_PATH%\\traductor.html\""
                bat "if exist \"${WORKSPACE_PATH}\\sistema_pedidos\\src\\main\\java\\docs\" xcopy \"${WORKSPACE_PATH}\\sistema_pedidos\\src\\main\\java\\docs\" \"%DESKTOP_PATH%\\docs\" /E /I"
            }
        }
    }
}
