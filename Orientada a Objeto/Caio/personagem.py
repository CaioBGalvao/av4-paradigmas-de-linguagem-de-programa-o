class Personagem:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__pontosVida = 100
        self.__pontosMana = 50

    def tomarDano(self, dano: int):
        nova_vida = self.__pontosVida - dano
        self.__pontosVida = max(nova_vida, 0)

    def curar(self, cura: int):
        nova_vida = self.__pontosVida + cura
        self.__pontosVida = min(nova_vida, 100)
