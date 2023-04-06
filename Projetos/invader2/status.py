class GameStats():
    ''' Armazena dados estatísticos do Jogo! '''

    def __init__(self, configs):
        ''' Inicializa os dados estatísticos. '''
        self.configs = configs
        self.reset_stats()

        # Inicia a Invasão alienígena em um estado ativo
        self.game_active = True

    def reset_stats(self):
        ''' Inicializa os dados estatísticos que podem mudar durante o jogo. '''
        self.nave_esquerda = self.configs.nave_limite
