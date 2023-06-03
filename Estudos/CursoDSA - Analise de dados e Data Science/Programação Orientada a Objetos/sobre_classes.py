class Livro():
    def __init__(self, titulo, isbn):

        # Este método vai inicializar cada objeto criado a partir desta classe
        # O nome deste método é __init__
        # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)

        # Podemos definir por padrão o nome dos atributos
        '''self.titulo = 'Sapiens - Uma breve história da humanidade'
        self.isbn = 958494
        print("Construtor chamado para criar um objeto desta classe.")'''

        # Ou então, podemos esclarecer os nomes dos atributos quando instânciar as classes
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")


    def imprime(self, titulo, isbn):
        # Métodos são funções que executam ações nos objetos da classe
        print(f"Foi criado o livro {titulo} com ISBN {isbn}")


# OBS: as funções dentro da classe são chamadas de >> MÉTODOS <<

# Criando uma instância da classe Livro
# Livro1 = Livro()

Livro2 = Livro("O poder do habito", 54976312)

# O objeto Livro1 é do tipo Livro
# print(f"Qual o tipo do objeto Livro1? =>> {type(Livro1)}")

# Chamando a nova instancia da classe Livro
Livro2.imprime("O poder do habito", 54976312)
