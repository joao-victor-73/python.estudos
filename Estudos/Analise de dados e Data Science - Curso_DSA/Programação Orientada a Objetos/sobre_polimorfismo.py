# Superclasse
class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass


# SubClasse 1
class Carro(Veiculo):

    def acelerar(self):
        print("O Carro está acelerando!")

    def frear(self):
        print("O Carro está freando!")


# SubClasse 2
class Moto(Veiculo):

    def acelerar(self):
        print("A Moto está acelerando!")

    def frear(self):
        print("A Moto está freando!")


# SubClasse 3
class Aviao(Veiculo):

    def acelerar(self):
        print("O Avião está acelerando!")

    def frear(self):
        print("O Avião está freando!")

    def decolar(self):
        print("O Avião está decolando!")


# Criando os objetos:
lista_veiculos = [Carro("Porsche", "911 Turbo"), Moto(
    "Honda", "CB 1000R"), Aviao("Boeing", "757")]

# Criando um looping:
for item in lista_veiculos:

    # O Método acelerar tem comportamento diferente dependendo do tipo de objeto
    item.acelerar()

    # O Método frear tem comportamento diferente dependendo do tipo de objeto
    item.frear()

    # Executamos o método decolar somente se o objeto for instância da Classe Aviao
    if isinstance(item, Aviao):
        item.decolar()

    print('============')
