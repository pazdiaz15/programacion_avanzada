pipeline {
    agent any
    parameters {
        string(name: 'ETAPA', defaultValue: '', description: 'Especifica qué etapa ejecutar')
    }
    stages {
        // stage('Javadoc Sistema Pedidos') {
        //     when { expression { params.ETAPA == 'javadoc_sistema_pedidos' } }
        //     steps {
        //         dir('sistema_pedidos/src/main/java/classes') {
        //             sh 'javadoc -d ../../../javadoc Main.java'
        //             sh 'ls -l'
        //         }
        //     }
        // }
        
        stage('PyDoc Traductor USQL') {
            when { expression { params.ETAPA == 'pydoc_traductor_usql' } }
            steps {
                    sh 'cd traductor_usql/src && python3 -m pydoc -w traductor'
                    sh 'ls -l'
                }
            }
        
        // stage('PyDoc Trivia') {
        //     when { expression { params.ETAPA == 'pydoc_trivia' } }
        //     steps {
        //         dir('trivia/src') {
        //             sh 'pydoc -w trivia'
        //             sh 'ls -l'
        //         }
        //     }
        // }

        stage('Archive') {
            steps {
                // archiveArtifacts allowEmptyArchive: true, artifacts: 'trivia/src/trivia.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'traductor_usql/src/traductor.html'
                // archiveArtifacts allowEmptyArchive: true, artifacts: 'sistema_pedidos/src/java/docs/Main.html'
            }
        }
    }
}
