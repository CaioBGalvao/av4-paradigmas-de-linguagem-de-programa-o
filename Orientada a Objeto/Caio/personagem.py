"""
Arquivo: personagem.py
Autor: Caio Barbosa Galvão
Objetivo: Define a classe 'Personagem' que serve como base
          para a simulação de aventura.
"""


class Personagem:
    """
    Representa um personagem em um jogo de RPG.

    Gerencia o estado do personagem (vida e mana) usando Propriedades
    Python (@property). Isso garante que as regras de negócio
    (como limites de vida/mana) sejam sempre aplicadas,
    não importa onde o valor seja alterado.
    """

    # --- Constantes de Classe ---
    # Definem as regras fixas para todos os personagens
    VIDA_MAXIMA = 100
    VIDA_MINIMA = 0
    MANA_MAXIMA = 50
    MANA_MINIMA = 0

    def __init__(self, nome: str):
        """
        Inicializa um novo Personagem.
        Os atributos com '__' (duplo underscore) são privados.
        """
        self.nome = nome  # Usa o @nome.setter para validar
        # Inicia o personagem com valores máximos
        self.__pontosVida = self.VIDA_MAXIMA
        self.__pontosMana = self.MANA_MAXIMA

    # --- Propriedade NOME ---
    @property
    def nome(self) -> str:
        """
        GETTER: Permite a leitura segura do atributo privado '__nome'.
        Ex: print(personagem.nome)
        """
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        """
        SETTER: É chamado automaticamente ao definir um valor.
        Ex: personagem.nome = "Novo Nome"
        Valida se o nome não está vazio.
        """

        # .strip() remove espaços em branco
        if novo_nome and novo_nome.strip():
            self.__nome = novo_nome.strip()
        else:
            # Garante que um personagem não pode ser criado sem nome
            raise ValueError("O nome não pode ser vazio")

    # --- Propriedade PONTOS DE VIDA ---
    @property
    def pontosVida(self) -> int:
        """
        GETTER: Permite a leitura segura do atributo privado '__pontosVida'.
        """
        return self.__pontosVida

    @pontosVida.setter
    def pontosVida(self, novo_valor: int):
        """
        SETTER: Garante que a vida nunca ultrapasse os limites.
        Esta é a lógica de "clamping" (fixação de valor).
        """
        # Ex: Se novo_valor for 110, min(100, 110) = 100
        # Ex: Se novo_valor for -10, max(0, -10) = 0
        self.__pontosVida = max(self.VIDA_MINIMA,
                                min(self.VIDA_MAXIMA, novo_valor))

    # --- Propriedade PONTOS DE MANA ---
    @property
    def pontosMana(self) -> int:
        """
        GETTER: Permite a leitura segura do atributo privado '__pontosMana'.
        """
        return self.__pontosMana

    @pontosMana.setter
    def pontosMana(self, novo_valor: int):
        """
        SETTER: Garante que a mana nunca ultrapasse os limites.
        Mesma lógica de "clamping" da vida.
        """
        self.__pontosMana = max(self.MANA_MINIMA,
                                min(self.MANA_MAXIMA, novo_valor))

    # --- MÉTODOS DE AÇÃO ---

    def tomarDano(self, dano: int):
        """
        Aplica dano ao personagem, subtraindo da vida.
        O @pontosVida.setter garante que a vida não ficará negativa.
        """
        if dano > 0:
            # Ao usar 'self.pontosVida', o setter é ativado
            self.pontosVida = self.pontosVida - dano

    def curar(self, cura: int):
        """
        Aplica cura ao personagem, somando à vida.
        O @pontosVida.setter garante que a vida não passará do máximo.
        """
        if cura > 0:
            # Ao usar 'self.pontosVida', o setter é ativado
            self.pontosVida = self.pontosVida + cura

    def usarMagia(self, custoMana: int) -> bool:
        """
        Tenta usar uma magia, consumindo mana.
        Retorna True se teve sucesso, False se não.
        """
        if custoMana <= 0:
            # Não se pode usar magia com custo zero ou negativo
            return False

        if self.pontosMana >= custoMana:
            # Sucesso: Tinha mana suficiente
            self.pontosMana = self.pontosMana - custoMana
            print(f"DEBUG: {self.nome} usou magia (custo {custoMana}).")
            return True
        else:
            # Falha: Mana insuficiente
            print(
                f"DEBUG: {self.nome} tentou, mas falhou (custo {custoMana})."
            )
            return False

    def estaVivo(self) -> bool:
        """
        Método utilitário para verificar se o personagem está vivo.
        Usado apenas no relatório final.
        """
        return self.pontosVida > self.VIDA_MINIMA
