class Personagem:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__pontosVida = 100
        self.__pontosMana = 50

    def tomarDano(self, dano: int):
        if dano >= self.__pontosVida:
            self.__pontosVida = 0
        else:
            self.__pontosVida -= dano

    def curar(self, cura: int):
        nova_vida = self.__pontosVida + cura
        self.__pontosVida = min(nova_vida, 100)
