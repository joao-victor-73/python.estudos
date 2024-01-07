# Criando a classe Animal (que vai ser a Super-Classe)
class Animal:

    def __init__(self):
        print("Animal Criado!")

    def imprimir(self):
        print("Este é um animal!")

    def comer(self):
        print("Hora de comer!")

    def emitir_som(self):
        pass


# Criando a classe Cachorro (que vai ser a Sub-Classe)
class Cachorro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado!")

    def emitir_som(self):
        print("Au Au!")


# Criando a classe Gatp (que vai ser outra Sub-Classe)
class Gato(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado!")

    def emitir_som(self):
        print("Miau Miau!")


# Criando os objetos (Instanciando as classes):
rex = Cachorro()
zeze = Gato()

rex.emitir_som()
zeze.emitir_som()

# Executando o método da classe Cachorro (Sub-Classe) que está na Super-Classe
rex.imprimir()

# Executando o método da classe Animal (Super-Classe)
rex.comer()
zeze.comer()