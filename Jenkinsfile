pipeline {
    agent any
    parameters {
        string(name: 'ETAPA', defaultValue: '', description: 'Especifica qué etapa ejecutar')
    }
    stages {
        stage('Javadoc Sistema Pedidos') {
            when { expression { params.ETAPA == 'javadoc_sistema_pedidos' } }
            steps {
                dir('sistema_pedidos/src/main/java/classes') {
                    sh 'javadoc -d ../../../javadoc Main.java'
                }
            }
        }
        
        stage('PyDoc Traductor USQL') {
            when { expression { params.ETAPA == 'pydoc_traductor_usql' } }
            steps {
                dir('traductor_usql/src') {
                    sh 'pydoc -w main'
                }
            }
        }
        
        stage('PyDoc Trivia') {
            when { expression { params.ETAPA == 'pydoc_trivia' } }
            steps {
                dir('trivia/src') {
                    sh 'pydoc -w trivia'
                }
            }
        }
    }
}
