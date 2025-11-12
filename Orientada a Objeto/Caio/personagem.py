class Personagem:
    """Representa um personagem em um jogo de RPG.

    Gerencia o estado do personagem usando Propriedades Python
    para garantir que as regras de negócio (limites de vida/mana)
    sejam sempre aplicadas de forma centralizada.
    """

    VIDA_MAXIMA = 100
    VIDA_MINIMA = 0
    MANA_MAXIMA = 50
    MANA_MINIMA = 0

    def __init__(self, nome: str):
        """Inicializa um novo Personagem."""
        self.nome = nome
        self.pontosVida = self.VIDA_MAXIMA
        self.pontosMana = self.MANA_MAXIMA

    # --- Propriedade NOME ---
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if novo_nome and novo_nome.strip():
            self.__nome = novo_nome.strip()
        else:
            raise ValueError("O nome não pode ser vazio")

    # --- Propriedade PONTOS DE VIDA ---
    @property
    def pontosVida(self) -> int:
        return self.__pontosVida

    @pontosVida.setter
    def pontosVida(self, novo_valor: int):
        self.__pontosVida = max(self.VIDA_MINIMA,
                                min(self.VIDA_MAXIMA, novo_valor))

    # --- Propriedade PONTOS DE MANA ---
    @property
    def pontosMana(self) -> int:
        return self.__pontosMana

    @pontosMana.setter
    def pontosMana(self, novo_valor: int):
        self.__pontosMana = max(self.MANA_MINIMA,
                                min(self.MANA_MAXIMA, novo_valor))

    # --- MÉTODOS DE AÇÃO ---

    def tomarDano(self, dano: int):
        """Aplica dano ao personagem."""
        if dano > 0:
            self.pontosVida = self.pontosVida - dano

    def curar(self, cura: int):
        """Aplica cura ao personagem."""
        if cura > 0:
            self.pontosVida = self.pontosVida + cura

    def usarMagia(self, custoMana: int) -> bool:
        """Tenta usar uma magia, consumindo mana."""
        if custoMana <= 0:
            return False

        if self.pontosMana >= custoMana:
            self.pontosMana = self.pontosMana - custoMana
            print(f"{self.nome} usou magia!")
            return True
        else:
            print(f"{self.nome} tentou usar magia, mas não tem mana!")
            return False

    def estaVivo(self) -> bool:
        """Verifica se o personagem está vivo."""
        return self.pontosVida > self.VIDA_MINIMA
