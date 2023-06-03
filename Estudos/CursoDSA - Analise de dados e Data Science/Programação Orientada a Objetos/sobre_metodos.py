# Criando uma classe chamada Circulo
class Circulo():

    # O valor de pi é constante
    pi = 3.14

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio=5):
        self.raio = raio

    def area(self):
        # Esse método calcula a área
        return (self.raio * self.raio) * Circulo.pi

    def setRaio(self, novo_raio):
        # Método para gerar um novo raio
        self.raio = novo_raio

    def getRaio(self):
        return self.raio


