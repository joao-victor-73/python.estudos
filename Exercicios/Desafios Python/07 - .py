"""27/05/2025

Desafio 7: Boletim Escolar por Matéria
    Você deve criar um programa que armazene as notas de vários alunos em várias matérias, e depois:
        -> Mostre a média de cada aluno.
        -> Mostre quem teve a maior média geral.
        -> Mostre quem teve a maior nota em Matemática.

    Estrutura de entrada sugerida:
        -> Use um dicionário onde:
            A chave é o nome do aluno.
            O valor é outro dicionário com as matérias e suas respectivas notas.
    
        Exemplo:
            alunos = {
                "Ana": {"Matemática": 8, "Português": 7, "História": 6},
                "Bruno": {"Matemática": 10, "Português": 8, "História": 9},
                "Carla": {"Matemática": 6, "Português": 9, "História": 10}
            }
        
        Saída Esperada (exemplo):
            Ana: média 7.0
            Bruno: média 9.0
            Carla: média 8.33

            Maior média geral: Bruno (9.0)
            Maior nota em Matemática: Bruno (10)

        
        Dicas:
            -> Use .items() para iterar sobre dicionários.
            -> Use sum() e len() para calcular médias.
            -> Use variáveis auxiliares para controlar maior média e maior nota.
"""
