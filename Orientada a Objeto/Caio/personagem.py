class Personagem:
    """Representa um personagem em um jogo de RPG.

    Esta classe gerencia os estados de vida e mana de um personagem,
    controlando as regras para tomar dano e ser curado.

    Attributes:
        __nome (str): O nome privado do personagem.
        __pontosVida (int): A contagem de vida privada, com máximo de 100.
        __pontosMana (int): A contagem de mana privada, com máximo de 50.
    """

    def __init__(self, nome: str):
        """Inicializa um novo Personagem.

        Args:
            nome (str): O nome que será atribuído ao personagem.
        """
        self.__nome = nome
        self.__pontosVida = 100
        self.__pontosMana = 50

    def tomarDano(self, dano: int):
        """Aplica dano ao personagem, limitando a vida mínima a 0.

        Calcula a nova vida subtraindo o dano e usa max() para garantir
        que o resultado nunca seja menor que 0.

        Args:
            dano (int): A quantidade de dano a ser aplicada.
        """
        nova_vida = self.__pontosVida - dano
        self.__pontosVida = max(nova_vida, 0)

    def curar(self, cura: int):
        """Aplica cura ao personagem, limitando a vida máxima a 100.

        Calcula a nova vida somando a cura e usa min() para garantir
        que o resultado nunca seja maior que 100.

        Args:
            cura (int): A quantidade de pontos de vida a serem restaurados.
        """
        nova_vida = self.__pontosVida + cura
        self.__pontosVida = min(nova_vida, 100)
