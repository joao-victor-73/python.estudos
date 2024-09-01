
class Jogo:
    def __init__(self, nome, categoria, console, id=None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.console = console


class Usuario:
    def __init__(self, id, nome, login_user, senha_user):
        self.id = id
        self.nome = nome
        self.login_user = login_user
        self.senha_user = senha_user

    # OBS: no meus estudos, o professor criou o id como login. Já eu aqui, criei o id como sendo P.K
    # Alterarei para que o login_user seja UNIQUE (01/09/24 - 00:12)