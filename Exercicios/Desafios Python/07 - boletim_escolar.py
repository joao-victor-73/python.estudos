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

lista_alunos = {
    "Ana": {"Matemática": 8, "Português": 7, "História": 6},
    "Bruno": {"Matemática": 10, "Português": 8, "História": 9},
    "Carla": {"Matemática": 6, "Português": 9, "História": 10}
}


def boletim_escolar(alunos):
    # Essa é a minha versão feita
    media_aluno = 0
    aluno_maior = "" 
    aluno_matematica = ""
    maior_matematica = 0

    for nome, infor in alunos.items():
        soma = sum(infor.values())
        
        media = soma / len(infor)
        
        for materia, nota in infor.items():
            soma += nota

            if media > media_aluno:
                media_aluno = media
                aluno_maior = nome    

            if materia == 'Matemática':
                if nota > maior_matematica:
                    maior_matematica = nota
                    aluno_matematica = f"O aluno {nome} tem a maior nota em matemática ({nota})"
                
        print(f"{nome} tem média {media:.1f}")

    print(f"O aluno {aluno_maior} tem a maior média da turma ({media_aluno})")
    print(aluno_matematica)



def boletim_escolar_chatgpt(alunos):
    # Esse é a função feita e ajustada pelo chatgpt

    maior_media = 0
    aluno_maior_media = ""
    maior_matematica = 0
    aluno_matematica = ""

    for nome, notas in alunos.items():
        soma = sum(notas.values())
        media = soma / len(notas)
        
        print(f"{nome} tem média {media:.1f}")

        if media > maior_media:
            maior_media = media
            aluno_maior_media = nome

        if notas["Matemática"] > maior_matematica:
            maior_matematica = notas["Matemática"]
            aluno_matematica = nome

    print(f"\nO aluno com a maior média geral é {aluno_maior_media} ({maior_media:.1f})")
    print(f"O aluno com a maior nota em Matemática é {aluno_matematica} ({maior_matematica})")




boletim_escolar(lista_alunos)
boletim_escolar_chatgpt(lista_alunos)