class Personagem:
    """Representa um personagem em um jogo de RPG.

    Gerencia o estado do personagem usando Propriedades Python
    para garantir que as regras de negócio (limites de vida/mana)
    sejam sempre aplicadas.
    """

    def __init__(self, nome: str):
        """Inicializa um novo Personagem.

        Args:
            nome (str): O nome que será atribuído ao personagem.
        """
        self.nome = nome  # Usa o setter de 'nome' logo no início
        self.__pontosVida = 100
        self.__pontosMana = 50

    # --- Propriedade NOME ---
    @property
    def nome(self) -> str:
        """Retorna o nome (privado) do personagem."""
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        """Define um novo nome, garantindo que não seja vazio."""
        if novo_nome and novo_nome.strip():
            self.__nome = novo_nome.strip()
        else:
            print("Erro: O nome não pode ser vazio.")
            # Em um código real, você poderia lançar uma exceção:
            # raise ValueError("O nome não pode ser vazio")

    # --- Propriedade PONTOS DE VIDA ---
    @property
    def pontosVida(self) -> int:
        """Retorna a quantidade de pontos de vida."""
        return self.__pontosVida

    @pontosVida.setter
    def pontosVida(self, novo_valor: int):
        """Define os pontos de vida, aplicando regras de limite (0 a 100)."""
        if novo_valor > 100:
            self.__pontosVida = 100
        elif novo_valor < 0:
            self.__pontosVida = 0
        else:
            self.__pontosVida = novo_valor

    # --- Propriedade PONTOS DE MANA ---
    @property
    def pontosMana(self) -> int:
        """Retorna a quantidade de pontos de mana."""
        return self.__pontosMana

    @pontosMana.setter
    def pontosMana(self, novo_valor: int):
        """Define os pontos de mana, aplicando regras de limite (0 a 50)."""
        if novo_valor > 50:
            self.__pontosMana = 50
        elif novo_valor < 0:
            self.__pontosMana = 0
        else:
            self.__pontosMana = novo_valor

    # --- MÉTODOS DE AÇÃO  ---

    def tomarDano(self, dano: int):
        """Aplica dano ao personagem."""
        self.pontosVida = self.pontosVida - dano

    def curar(self, cura: int):
        """Aplica cura ao personagem."""
        self.pontosVida = self.pontosVida + cura

    def usarMagia(self, custoMana: int) -> bool:
        """Tenta usar uma magia, consumindo mana.

        Retorna True se bem-sucedido, False caso contrário.
        """
        if self.pontosMana >= custoMana:
            self.pontosMana = self.pontosMana - custoMana
            return True
        else:
            print(f"{self.nome} tentou usar magia, mas não tem mana!")
            return False

    def estaVivo(self) -> bool:
        """Verifica se o personagem está vivo."""
        return self.pontosVida > 0
