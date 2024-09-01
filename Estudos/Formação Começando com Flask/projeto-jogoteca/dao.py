from models import Jogo, Usuario

SQL_DELETA_JOGO = "DELETE FROM jogos WHERE id = %s"
SQL_JOGO_POR_ID = "SELECT id, nome, categoria, console FROM jogos WHERE id = %s"
SQL_USUARIO_POR_ID = "SELECT id, nome, login_user, senha_user FROM usuarios WHERE login_user = %s"
SQL_ATUALIZA_JOGO = "UPDATE jogos SET nome=%s, categoria=%s, console=%s WHERE id = %s"
SQL_BUSCA_JOGOS = "SELECT id, nome, categoria, console FROM jogos"
SQL_CRIA_JOGO = "INSERT INTO jogos(nome, categoria, console) VALUES (%s, %s, %s)"


class JogoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, jogo):
        cursor = self.__db.cursor()

        if (jogo.id):
            cursor.execute(SQL_ATUALIZA_JOGO,
                           (jogo.nome, jogo.categoria, jogo.console, jogo.id))
        else:
            cursor.execute(SQL_CRIA_JOGO, (jogo.nome,
                           jogo.categoria, jogo.console))
            jogo.id = cursor.lastrowid

        self.__db.commit()
        return jogo

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduz_jogos(cursor.fetchall())
        return jogos

    def buscar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_JOGO_POR_ID, (id,))
        dict = cursor.fetchone()
        # Esse metodo retorna os registros em dicionários e não tuplas, ja na outra API (MySQLdb),
        # ele retorna os registros como uma tupla

        return Jogo(dict['nome'], dict['categoria'], dict['console'], id=dict['id'])

    def deletar(self, __id):
        self.__db.cursor().execute(SQL_DELETA_JOGO, (id, ))
        self.__db.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_jogos(jogos):
    def cria_jogo_com_dict(dict):
        return Jogo(dict['nome'], dict['categoria'], dict['console'], id=dict['id'])
    return list(map(cria_jogo_com_dict, jogos))


def traduz_usuario(dict):
    return Usuario(dict['id'], dict['nome'], dict['login_user'], dict['senha_user'])
