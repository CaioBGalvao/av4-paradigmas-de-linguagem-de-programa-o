"""
Arquivo: aventura.py
Autor: Caio Barbosa Galvão
Objetivo: Executa uma narrativa de batalha linear e determinística.
"""

# Importa a classe 'Personagem' do arquivo 'personagem.py'
from personagem import Personagem

# Importa a biblioteca 'time' para adicionar pausas dramáticas
import time

# Importa o tipo 'List' para usar nas dicas de tipo (type hints)
from typing import List

# Constante para a pausa (em segundos) entre as ações
PAUSA_NARRATIVA = 2.0


def mostrar_status_final(
    time_j: List[Personagem], time_i: List[Personagem]
) -> None:
    """
    Função auxiliar para exibir o "Relatório de Batalha" no final.
    Ela formata a saída para ficar alinhada e fácil de ler.

    :param time_j: Uma lista de objetos Personagem (time do jogador)
    :param time_i: Uma lista de objetos Personagem (time inimigo)
    """
    print("\n" + "=" * 45)
    print("RELATÓRIO FINAL DA BATALHA:")

    print("\n  SEU TIME:")
    for p in time_j:
        status_vida = f"HP: {p.pontosVida:3}/{p.VIDA_MAXIMA}"
        status_vivo = "[VIVO]" if p.estaVivo() else "[MORTO]"
        print(f"    {p.nome:<18} | {status_vida} {status_vivo}")

    print("\n  TIME INIMIGO:")
    for p in time_i:
        status_vida = f"HP: {p.pontosVida:3}/{p.VIDA_MAXIMA}"
        status_vivo = "[VIVO]" if p.estaVivo() else "[MORTO]"
        print(f"    {p.nome:<18} | {status_vida} {status_vivo}")
    print("=" * 45 + "\n")


def main() -> None:
    """
    Função principal que contém toda a lógica do programa.
    Não retorna nenhum valor.
    """

    print("--- SIMULADOR DE AVENTURA (VERSÃO NARRATIVA) ---")
    print("Por favor, defina os nomes dos seus 3 heróis.")

    # --- 1. CONFIGURAÇÃO: Pedir Nomes ---
    try:
        nome_mago_j = input("Nome do seu Mago: ")
        nome_guerreiro_j = input("Nome do seu Guerreiro: ")
        nome_sacerdote_j = input("Nome do seu Sacerdote: ")

        # --- 2. PREPARAÇÃO: Criar Personagens ---

        # Time do Jogador
        mago_j = Personagem(nome_mago_j)
        guerreiro_j = Personagem(nome_guerreiro_j)
        sacerdote_j = Personagem(nome_sacerdote_j)

        time_jogador: List[Personagem] = [
            mago_j,
            guerreiro_j,
            sacerdote_j,
        ]

        # Time Inimigo
        mago_i = Personagem("Mago Maligno")
        guerreiro_i = Personagem("Orc Bruto")
        sacerdote_i = Personagem("Clérigo das Sombras")

        time_inimigo: List[Personagem] = [
            mago_i,
            guerreiro_i,
            sacerdote_i,
        ]

    except ValueError as e:
        print(f"\nERRO: {e}. O nome não pode ser vazio.")
        print("A aventura foi cancelada.")
        return

    # --- 3. EXECUÇÃO: A Narrativa Linear ---

    print("\n" + "*" * 40)
    print("A BATALHA COMEÇA!")
    print("*" * 40 + "\n")
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 1: Mago (Jogador) ---
    print(
        f"🔥 O time um começa! {mago_j.nome} joga uma 'Bola de Fogo' "
        f"no {guerreiro_i.nome}!"
    )
    mago_j.usarMagia(15)
    guerreiro_i.tomarDano(35)
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 2: Guerreiro (Jogador) ---
    print(
        f"\n⚔️ {guerreiro_j.nome} avança contra o {guerreiro_i.nome}, "
        f"que já está machucado."
    )
    print("Eles trocam golpes ferozes!")
    guerreiro_j.tomarDano(20)
    guerreiro_i.tomarDano(25)
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 3: Sacerdote (Jogador) ---
    print(
        f"\n✨ {sacerdote_j.nome} se precipita! Ele gasta muita mana "
        f"tentando curar {guerreiro_j.nome} cedo demais."
    )
    sacerdote_j.usarMagia(30)
    guerreiro_j.curar(10)
    print("A maior parte da cura foi desperdiçada!")
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 4: Sacerdote (Inimigo) ---
    print(
        f"\n💖 O {sacerdote_i.nome} inimigo é mais paciente. "
        f"Ele espera {guerreiro_i.nome} ficar ferido..."
    )
    print("E então usa uma 'Cura Sombria' poderosa, recuperando muita vida!")
    sacerdote_i.usarMagia(15)
    guerreiro_i.curar(50)
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 5: Guerreiro (Inimigo) ---
    print(
        f"\n🔨 Agora em desvantagem, {guerreiro_j.nome} enfrenta 3 inimigos."
    )
    print(f"O {guerreiro_i.nome} o ataca, e {guerreiro_j.nome} não resiste...")
    guerreiro_j.tomarDano(80)
    print(f"!!! {guerreiro_j.nome} foi derrotado !!!")
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 6: Mago (Inimigo) ---
    print(
        f"\n❄️ É a vez do {mago_i.nome}! Ele lança uma 'Seta de Gelo' "
        f"contra {mago_j.nome}!"
    )
    mago_i.usarMagia(10)
    mago_j.tomarDano(30)
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 7: Mago (Jogador) ---
    print(
        f"\n🩹 {mago_j.nome} vê a situação e usa uma poção de cura, "
        f"mas ela não cura muito."
    )
    mago_j.curar(20)
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 8: Sacerdote (Inimigo) ---
    print(
        f"\n⛪ O {sacerdote_i.nome} inimigo avança com uma maça "
        f"contra {sacerdote_j.nome}!"
    )
    sacerdote_j.tomarDano(25)
    time.sleep(PAUSA_NARRATIVA)

    # --- TURNO 9: O Fim ---
    print(f"\n🔥 {mago_j.nome} tenta uma última magia, mas é interrompido.")
    print(
        f"⛪ {sacerdote_j.nome} tenta defender seu mago, "
        f"mas é sobrepujado..."
    )

    sacerdote_j.tomarDano(75)
    mago_j.tomarDano(90)

    print(f"!!! {sacerdote_j.nome} e {mago_j.nome} são derrotados !!!")
    time.sleep(PAUSA_NARRATIVA)

    # --- 4. CONCLUSÃO: Relatório Final ---

    print("\n" + "*" * 40)
    print("A BATALHA TERMINOU!")
    print("*" * 40)

    mostrar_status_final(time_jogador, time_inimigo)

    print("RESULTADO: O time inimigo venceu a batalha.")
    print("*" * 40)


# --- Ponto de Entrada do Script ---
if __name__ == "__main__":
    main()
