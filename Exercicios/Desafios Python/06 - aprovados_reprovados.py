""""26/05/2025 - Desafio traz tuplas e listas combinadas para práticar

Desafio 06: Alunos aprovados e reprovados
    Crie um programa que receba uma lista de tuplas, onde cada tupla contém o nome de um aluno e sua nota final (de 0 a 10).
    Você deve:
        -> Separar os alunos aprovados (nota ≥ 6) dos reprovados (nota < 6).
        -> Retornar duas listas:
        -> Uma com os nomes dos aprovados.
        -> Outra com os nomes dos reprovados.
        -> Exibir também a média geral da turma.
    
    Exemplo de entrada:
        alunos = [
            ("Ana", 7.5),
            ("Bruno", 5.0),
            ("Carlos", 8.0),
            ("Daniela", 4.5),
            ("Eduardo", 6.0)
        ]
    

    Saída Esperada:
        Aprovados: ['Ana', 'Carlos', 'Eduardo']
        Reprovados: ['Bruno', 'Daniela']
        Média da turma: 6.2

        
    REGRAS:
        -> Use estruturas como listas e tuplas.
        -> Faça validações se quiser (ex: ignorar notas inválidas).
        -> Se quiser, pode deixar os nomes em ordem alfabética.
"""

alunos_lista = [
    ('Paulo', 8.6), ('Marcia', 9.0), ('Francisco', 5.0), 
    ('Eduardo', 10.0), ('Bruno', 1.8), ('Carlos', 7.4), 
    ('Daniela', 9.8)
    ]

def aprovados_reprovados(alunos):
    media = 0 
    soma = 0
    aprovados = []
    reprovados = []


    for aluno in alunos:
        nome, nota = aluno
        # Aqui é a mesma coisa que dizer que nome é aluno[0]
        # e nota é aluno[1]

        
        if nota[1] >= 7:
            aprovados.append(nome)
        else:
            reprovados.append(nome)

        soma += nota
    
    media = soma / len(alunos)
    
    return aprovados, reprovados, media

apro, repro, media_turma = aprovados_reprovados(alunos_lista)

print(f"Alunos Aprovados:  {apro}")
print(f"Alunos Reprovados: {repro}")
print(f"A média da turma foi: {media_turma:.2f}")
